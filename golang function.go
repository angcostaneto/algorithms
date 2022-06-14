/* Function Description

Complete the introTutorial function in the editor below. It must return an integer representing the zero-based index of V.

introTutorial has the following parameter(s):

int arr[n]: a sorted array of integers
int V: an integer to search for
Returns

int: the index of V in  */

func introTutorial(V int32, arr []int32) int32 {
    // Write your code here    
    for key, value := range arr {
        if value == V {
            return int32(key)
        }
    }
    
    return int32(0)
}
