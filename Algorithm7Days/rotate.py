
'''
题目要求
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

nums = [1,2,3,4,5,6,7]
k = 3
def rotate_1(nums,k):
    '''
    :param nums: 输入数据组
    :param k: 反转最后三个数
    :return:
    '''
    for i in range(k):
        tmp = nums[-1]
        for j in range(len(nums)-1,0,-1):
            print(j)
            nums[j] = nums[j-1]
        nums[0] = tmp
    print(nums)
    return nums


def rotate_2(nums,k):
    '''
    :param nums:
    :param k: 插入反转
    :return:
    '''
    n = len(nums)
    k %=n
    for _ in range(k):
        nums.insert(0,nums.pop())
    print(nums)

rotate_2(nums,k)


def rotate_3(nums,k):
    '''
    :param nums:
    :param k:
    :return:
    '''
    size = len(nums)
    _nums = [num for num in nums]
    for i in range(size):
        nums[(i+k)%size] = _nums[i]
    print(nums)


def rotate_4(nums,k):
    '''
    :param nums:
    :param k: 拼接
    :return:
    '''
    k %= len(nums)
    nums[:] = nums[-k:]+nums[:-k]
    print(nums)

def rotate_5(nums,k):
    '''
    :param nums:
    :param k: 三重反转
    :return:
    '''
    n = len(nums)
    k %= n
    nums[:] = nums[::-1]
    nums[:k]= nums[:k:][::-1]
    nums[k:]=nums[k::][::-1]

