class Solution:
    def my_grocery_list(self,str1,str2):
    # type str1:string
    # type str2: string
    # return: list

        final_list = []
        list1 = str1.split(' ')
        list2 = str2.split(' ')
        for item in list1:
            if item not in final_list and item != '':
                final_list.append(item)
        for item in list2:
            if item not in final_list and item != '':
                final_list.append(item)
        return final_list
def main():
    string1 = input()
    string2 = input()

    tc1 = Solution()
    ans = tc1.my_grocery_list(string1,string2)
    print(ans)

if __name__ == "__main__":
     main()
