class file_explorer():
    def __init__(self):
        with open('/Users/wtrott/Downloads/input1207.txt') as file:
            data = [line.replace('\n', '' )for line in file]
        self.files = [line for line in data if line.split(' ')[0].isdigit()]
        self._build_structure(data)
        self._directory_sizes()
        
    def _build_structure(self, input_data):
        self.file_sizes = {}
        current_directory = None
        file_path = []
        for line in input_data:
            command = line.split(' ')
            if 'cd' == command[1]:
                dir_change = command[-1]
                if dir_change == '/':
                    continue
                elif dir_change != '..':
                    file_path.append(dir_change)
                else:
                    file_path.pop()
            elif command[0].isdigit():
                if file_path:
                    self.file_sizes[f"home/{'/'.join(file_path)}/{command[1]}"] = int(command[0])
                else:
                    self.file_sizes[f"home/{command[1]}"] = int(command[0])
    
    def _directory_sizes(self):
        self.directory_size = {}
        for file, size in self.file_sizes.items():
            directories = file.split('/')[:-1]
            for level in range(len(directories)):
                directory_path = '/'.join(directories[:level + 1])
                if self.directory_size.get(directory_path):
                    self.directory_size[directory_path] += size
                else:
                    self.directory_size[directory_path] = size
                
            
                
    def problem_1(self):
        total_size = 0
        for directory, size in self.directory_size.items():
            if size <= 100000:
                total_size += size
        print(f"Total size of directories less than 100000 in size: {total_size}")
    
    def problem_2(self):
        free_space = 70000000 - self.directory_size['home']
        print(f"Minimum size dir to delete: {min([size for size in self.directory_size.values() if free_space + size > 30000000])}")
                    
explorer = file_explorer()
explorer.problem_1()
explorer.problem_2()
