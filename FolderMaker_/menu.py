from FolderMaker_ import foldermaker
menubar = nuke.menu("Nuke")
m = menubar.addMenu("Yesh")
m.addCommand("Make My Folder", foldermaker.main)