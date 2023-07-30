import json
from datetime import datetime
import requests
import time
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('Service Monitor')


def get_conf(typ):
    f = open(f'{typ}.json')
    data = json.load(f)
    f.close()
    return data


if __name__ == '__main__':
    start_time = time.perf_counter()
    log.info('program is starting')
    conf = get_conf('conf')
    sleep_seconds = conf['sleep_seconds']
    batch_size = conf['batch_size']
    reload_seconds = conf['reload_seconds']
    urls = get_conf('urls')
    results = []
    while True:
        for url in urls:
            response = requests.get(url['url'])
            result = {"ts": datetime.utcnow().isoformat(), "url": url['url'], "status_code": response.status_code,
                      "latency": response.elapsed.microseconds}
            results.append(result)
            log.debug(result)
        if len(results) >= batch_size:
            # save data
            log.info(f'saving data since {str(len(results))} >= {batch_size}')
            log.info('clearing results')
            results.clear()

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        if elapsed_time >= reload_seconds:
            log.info('reloading urls')
            urls.clear()
            urls = get_conf('urls')
            start_time = time.perf_counter()

        log.info(f'sleeping for: {sleep_seconds}')
        time.sleep(sleep_seconds)
