from globalSetting import *
from utils import *

def parserSetting():
    parser = argparse.ArgumentParser(description="--bench benchName")
    parser.add_argument(
            "--bench",
            type = str,
            nargs = 1,
            default = 'bessel_Jnu',
            help = 'Check ../data/* for all the benchmarks.'
            )
    args = parser.parse_args()
    benchName = args.bench[0]
    return args

def configSetting():
    global c
    print("config loadding")        
    c = json.load(open(configPath,'r'))
    configSavedPath = os.path.join(workDir, 'config.json')
    configSavedFile = open(configSavedPath, 'w')
    json.dump(c, configSavedFile, sort_keys=False, indent=4)

def logSetting():
    logging.basicConfig(
        filename=logPath,
        filemode="a+",
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%y/%m/%d_%H:%M:%S",
        level=logging.DEBUG
    )
    logging.debug("test log function")

def dataReading():
    print ("data reading")

def modelLoading():
    print ("model loading")
    
if (__name__=="__main__"):
    print ("Process begins")
    parserSetting()
    configSetting()
    logSetting()
    dataReading()
    modelLoading()
    logging.info("initiation done")
    
    
