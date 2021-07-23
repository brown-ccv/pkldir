import argparse
import pickle
import os 


def main():
    parser = argparse.ArgumentParser(description = """
        This is a simple command-line tool used to pickle the contents of a directory. 
        The original file and directory are left unchanged; this tool creates a duplicate 
        directory with "-pkl" appended and containing pickled versions of all 
        original files.""")

    parser.add_argument("dir", help = "This is the directory containing the files to be pickled")

    input_dir = parser.parse_args().dir 

    files = os.listdir(input_dir)

    output_dir = input_dir + "-pkl"
    os.mkdir(output_dir)

    for filename in files: 
        with open(os.path.join(input_dir, filename), "rb") as f:
            text = f.read()
            
        pickle.dump(text, open(os.path.join(output_dir, "-pkl" + filename), "wb"))

if __name__ == "__main__":
    main()