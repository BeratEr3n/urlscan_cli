# src/core/poller.py

import time
from core.api import APIClient
from config.settings import SCAN_INTERVAL, SCAN_TIMEOUT


class UrlScanPoller:
    """
    urlscan.io scan sonucunu bekleyen poller.
    """

    def __init__(
        self,
        client: APIClient,
        interval: int = SCAN_INTERVAL,
        timeout: int = SCAN_TIMEOUT,
    ):
        """
        :param interval: kaç saniyede bir result endpoint'i poll edilecek
        :param timeout: maksimum bekleme süresi (saniye)
        """
        self.client = client
        self.interval = interval
        self.timeout = timeout

    def wait(self, scan_id: str) -> dict:
        """
        Scan sonucu hazır olana kadar bekler.
        Hazır olduğunda result JSON döner.
        """

        start_time = time.time()

        while True:
            try:
                response = self.client.get(
                    path=f"/result/{scan_id}/"
                )
                # 200 geldiyse buraya düşer
                return response

            except RuntimeError as e:
                message = str(e)

                # 404 → scan hala çalışıyor
                if "HTTP 404" in message:
                    print("Üzerinde Çalışılıyor : ",int(time.time() - start_time), "sn")
                    pass

                # 410 → scan silinmiş
                elif "HTTP 410" in message:
                    raise RuntimeError(
                        f"Scan result deleted for scan_id={scan_id}"
                    )

                else:
                    # bilinmeyen hata
                    raise

            if time.time() - start_time > self.timeout:
                raise TimeoutError(
                    f"Scan did not finish within {self.timeout} seconds"
                )

            time.sleep(self.interval)
