from random import randint


"""
    Important points about code
        * Testing for this code could be improved by using a list of non-integers, real numbers or strings

"""

class sorter:
    """sorter base class"""
    def __init__(self):
        pass

    def sort(self):
        print("function to sort a list")

class InsertionSorter(sorter):
    """A class for insertion sort, inherits the sort method from the sorter class"""

    def sort(self, unsortedArray) -> list:
        value = 0
        index = 0

        for i in range(1, len(unsortedArray)): #loop from the second element to the last
            value = unsortedArray[i] #store the current temporary value
            index = i #store the current position in the array - this will be used as a starting point to count backwards during the comparisons

            while (index > 0) and (value < unsortedArray[index - 1]): #continue comparing previous values in the list with the temporary value until this start of the array is reached or the two values are in the correct order
                unsortedArray[index] = unsortedArray[index - 1] #this compared value to copied into the element to the right
                index -= 1 #decrement the element being compared next

            unsortedArray[index] = value #the temporary value is copied into the correct place

        return unsortedArray


class BubbleSorter(sorter):
    """A class for bubble sort, inherits the sort method from the sorter class"""

    def sort(self, unsortedArray) -> list:
        n = len(unsortedArray) #the length of the array is stored in a variable
        swapped  = True #set a flag variable to note if a swap has been made
        while swapped and n >= 0:
            swapped = False #set the flag variable to note if a swap has been made
            for i in range(0, n - 1): #loop from the first element to the penultimate array element
                if unsortedArray[i] > unsortedArray[i + 1]: #compare two adjacent values
                    #swap the variables if they are not in the correct order
                    temp = unsortedArray[i]
                    unsortedArray[i] = unsortedArray[i + 1]
                    unsortedArray[i + 1] = temp
                    swapped = True #set the flag variable to note if a swap has taken place
            n -= 1 #each fixed loop reduces the iterations by one as one more element is sorted correctly at the end of the array

        return unsortedArray

class searcher:
    """searcher base class"""

    def __init(self):
        pass

    def search(self):
        print("function to search a list")


def generateRandomArray(length) -> list:
    """
    Generates a random array of a given length
    Parameters
    ----------
    length : int
        the length the list is to be

    Returns
    -------
    list
        a list full of random integers

    """
    randomArray = []
    for i in range(length):
        num = randint(1,100)
        randomArray.append(num)
    return randomArray


def testSorter(sorter) -> bool:
    """
    Tests a sorter and serves as a method of component testing
    Parameters
    ----------
    sorter : sorter
        a sorter object constructed from a sorter class

    Returns
    -------
    bool
        True if sorter works
    """
    testData = generateRandomArray(50)
    print("unsorted", testData)
    sortedData = sorter.sort(testData)
    print("sorted", sortedData)
    worked =  (sortedData == sorted(sortedData))

    print("was successful", worked)
    return worked



insertion = InsertionSorter()

testSorter(insertion)

bubble = BubbleSorter()
testSorter(bubble)
