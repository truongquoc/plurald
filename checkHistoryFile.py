def get_courses():
    """Parsing courselist.txt
    
    Arguments:
        scriptpath {str} -- Absolute path to script directory
    
    Returns:
        [str] -- List of course identifiers exposed by courselist.txt
    """
    # courses textfile prelocated inside script directory
    filelist = "courselist.txt"
    current_file = open("courselist.clone.txt", "r")
    
    courses = []
    current_courses = []
    for line in current_file.readlines():
        current_courses.append(line.strip())
    try:
        with open("courselist.txt", 'r+') as file:
            for line in file.readlines():
                if(line.strip() in current_courses):
                    continue
                courses.append(line.strip())
                # if re.search(r'\S', line):
        return courses
    except FileNotFoundError:
        print("There is no courselist.txt in script path. Terminating script ...")

def main():
    available_courses = get_courses()
    print(available_courses)
    if available_courses: 
        for course in available_courses:
            with open("courselist.clone.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(course)
if __name__ == "__main__":
    main()