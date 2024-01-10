import csv

class ExportCSV:
    def __init__ (self, file_path, arr = None):
        self.file_path = file_path
        self.arr = arr

    def set_arr(self, arr):
        self.arr = arr
    
    def export(self):
        with open(self.file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for array in self.arr:
                csv_writer.writerow([str(cell) for row in array for cell in row])
