import os
import logging
import argparse

# Argument Parser
parser = argparse.ArgumentParser(description="Rename Files")
parser.add_argument("--path", type=str, required=True, 
                    help="Directory path where files are to be renamed")
parser.add_argument("--debug", action="store_true", 
                    help="If True then print DEBUG Info")
parser.add_argument("--prefix", type=str, 
                    help="If provided, then file would be renamed as Prefix+n \
                    where n is number from 1 to number of files present in directory")
args = parser.parse_args()

# Setting Logger
logging.basicConfig(filename="log_file.log", filemode="w", 
                    format="%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s")
log = logging.getLogger()
if args.debug is True:
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.INFO)

def rename_files_in_directory(path, prefix_str):
    try:
        file_names = os.listdir(path)
        log.info(file_names)
        for i in range(1, len(file_names)+1):
            if os.path.isfile(org_file_path := (path+"/"+file_names[i-1])):
                if prefix_str is not None:
                    log.debug(f"{org_file_path}, {path}+'/'+{prefix_str}+'_'+{str(i)}")
                    os.rename(org_file_path, path+"/"+prefix_str+"_"+str(i))
                else:
                    log.debug(f"{org_file_path}, {path}+'/'+{str(i)}")
                    os.rename(org_file_path, path+"/"+str(i))
            else:
                log.warning(f"Directory Found: {org_file_path}")
        log.info("Success...Files have been renamed")
    except FileNotFoundError as err:
        log.error("Directory Not Found")
        log.exception(err)
        raise
    except Exception as err:
        log.exception(err)
        raise

if __name__ == "__main__":
    rename_files_in_directory(args.path, args.prefix)
