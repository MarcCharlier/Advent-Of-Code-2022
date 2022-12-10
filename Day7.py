import anytree

with open('filesystem.txt') as fs:
    fs_line = str.strip(fs.readline())
    fs_root_folder = anytree.AnyNode(id="fs_root", foldersize=0)
    new_folder = fs_root_folder
    while True:
        fs_line = str.strip(fs.readline())
        if not fs_line: break
        if fs_line != "$ ls" and fs_line[0:3] != "dir":
            if fs_line[0:4] == "$ cd" and fs_line != "$ cd ..":
                parent_folder = new_folder
                new_folder = anytree.AnyNode(id=fs_line[5:], parent=parent_folder, foldersize=0)
            elif fs_line == "$ cd ..":
                new_folder = new_folder.parent
            elif fs_line[0].isdigit():
                new_folder.foldersize += int((fs_line[0:fs_line.find(" ")]))
                update_parent_folder = new_folder
                while update_parent_folder.id != "fs_root":
                    update_parent_folder = update_parent_folder.parent
                    update_parent_folder.foldersize += int((fs_line[0:fs_line.find(" ")]))

print(anytree.RenderTree(fs_root_folder))
small_folder_list = anytree.findall(fs_root_folder, filter_=lambda node: node.foldersize <= 100000)
total_small_size = 0
for small_folder in small_folder_list: total_small_size += small_folder.foldersize
print(str(total_small_size))
all_folders_list = list(anytree.findall(fs_root_folder))
all_folders_list.sort(key=lambda x: x.foldersize)
print(all_folders_list)

