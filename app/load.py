import configparser

conf = {

}

def load_conf():
    cfg = configparser.ConfigParser()
    cfg.read("../dontneedit.ini")
    conf["TOKEN"] = cfg["Discord"]["TOKEN"]
    return conf