from utils import loadConfig
from table1_logic import processTable1Data
from table2_logic import processTable2Data
import threading


def main() -> None:
    """
    Main Application
    """
    config = loadConfig()

    t1 = threading.Thread(target=processTable1Data, args=(config,))
    t2 = threading.Thread(target=processTable2Data, args=(config,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
