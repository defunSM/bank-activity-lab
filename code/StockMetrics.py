
import statistics as stats

from code.StockData import StockData

class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        numeric_rows = [ val[1:] for val in self.data ]

        for row in numeric_rows:

            # compute average

            cleaned_rows = [ float(val.strip()) for val in row if (val != ' ' and val != '') ]
            length = len(cleaned_rows)

            avg = sum(cleaned_rows) / length
            averages.append(round(avg, 3))

        return averages

    def median02(self):
        """pt2
        """
        medians = []
        numeric_rows = [ val[1:] for val in self.data ]
        
        for row in numeric_rows:
            
            # sorts and cleans the rows removing spaces and empty strings
            cleaned_rows = [ float(val.strip()) for val in row if (val != ' ' and val != '') ]
            cleaned_rows = sorted(cleaned_rows)
            length = len(cleaned_rows)

            # if even amount of numbers it finds the middle number between the two numbers left and right mid point
            if length % 2 == 0:
                mid = length // 2
                medians.append(float( cleaned_rows[mid] + cleaned_rows[mid - 1]) / 2)
            else:
                mid = length // 2
                medians.append(float(cleaned_rows[mid]))

        return medians

    def stddev03(self):
        """pt3
        """

        stddev = []
        numeric_rows = [ val[1:] for val in self.data ]

        for row in numeric_rows:

            # calculate the average

            cleaned_rows = [ float(val.strip()) for val in row if (val != ' ' and val != '') ]
            length = len(cleaned_rows)

            average = sum(cleaned_rows) / length

            # compute std

            std_computation_part1 = [(val - average)**2 for val in cleaned_rows]
            std = (sum(std_computation_part1) / (length - 1))**(0.5)

            stddev.append(round(std, 3))
        
        return stddev
