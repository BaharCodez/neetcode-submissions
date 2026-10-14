A hashmap because why do i keep forgetting this:

seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        return [seen[complement], i]

    seen[num] = i

How many times have I seen this?

count[x] = count.get(x, 0) + 1

Where did I see this?

seen[x] = i

Sliding window:

Fixed size:

for right in range(len(nums)):
    # add nums[right]

    if right >= k:
        # remove nums[right - k]

    if right >= k - 1:
        # process window

variable size:

left = 0

for right in range(len(nums)):
    # add nums[right]

    while window_is_invalid:
        # remove nums[left]
        left += 1



string-encode-and-decode (5/10):





Key Idea: start with empty str,  += len(word + # and our words into it for encode. For decode, start with empy arr and pointer. then 2 pointer until #, after that we append the length of the word after that pointer and move the first pointer up

Longest Consecutive (I need to optimise)





Key Idea: Have a set of numbers, if theres a consecutive number smaller we skip this number, else we add its length

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        longest = 0
        
        for num in numset:
            length = 0
            if num -1 not in numset:
                length = 1

                while length + num in numset:
                    length +=1

            if length > longest:
                longest = length    


IMPORTANT STYLING NOTE:

I tend to use if statements when max or min could be used be aware!

findMin():

This one I did surprisingly worst than I expected. The bit I fumbled was overcomplicating ef/ else statements, I was trying to use elif when else covered every thing I needed because monotnically increasing. Here drawing it out aided a lot.

Looping with linked list:

while curr is enough no null no empty

hasCycle:
fast and slow pointers, for every 1 next for slow fast goes next next. I tripped up a bit on the loop while fast and fast.next:

Dummy nodes:

dummy = ListNode()
current = dummy

and then returning dummy.next. I had the same pattern intuitively however the logistics were not working without dummy.

Reoder list-

Three main ideas- find middle, reverse the second half of the algorithm, then merge it

This makes it so much easier to manage.

I got stuck with the merging bit quite a lot, but its the same as logic as the reversing but u point to each other

Koko Eating Bananas-

I suffered here, understanding this problem took quite a bit of time, and figuring out where to actually use binary search was also difficult. Conce[ptually I struggled with 

hours += math.ceil(float(p)/ k)

but I forgot you need to consecutively add until it reaches the max hours. Looking back at hindsight it wasn't too difficult however I struggled with technique of adding up the hours and comparing using binary search

Two sum:

I know this is so late for 2sum but I struggle to conceptualize how hashing works, forexample to add to a hashset I owuld have done seen[need] = i, the indexing and the actual implementation is quite confusing and something I just need to practise. I also am very bad at using enumerate 

for i, x in enumerate(nums)

-- COMEACK TO THIS 

Longest repeating character:

 learnt some theory for sliding window, I did well with the actual problem solving but struggled to practically show it for example: 

count[char] = count.get(char, 0) + 1
 # brain didn't like this
 # means: Get the current count → use 0 if it doesn't exist → add 1 → save it.

Also the hated for r, char enumerate failed it again

lengthOfLongestSubstring:

Conceptually easier than the last one however I forgot sliding window template is this type of loop 

for r in range(len(s)):

and we stop the window when

while s[r] in seen:
                seen.remove(s[l]); l += 1

but thats just the basics of sliding window.

Permutation in String:

I didn't like the sliding window answer, I made a solution that was suboptimal with Time:  O(n · m log m) - because for loop O(n),  sorting substring = O(mlogm)

for r in range(len(s2) - size + 1):
    substring = s2[r : r + size]

    if sorted(substring) == sorted(s1):
        return True

Space: O(m) - due to using sorted ()

Remove Nth Node From End of List:"

I liked this one, conceptually talked it out with gpt and it was locked in huzzah. I failed the dummy bit though. The edge case. I (1) for get to return dummy.next instead of head and also to set ListNode(0) in the first place too. All good

Invert Binary Tree

My first graph question everr: 

Struggled on the formatting and how you call itself becuase I had never done it before but conceptually was easy (recursive DFS).  Time complexity O(n) , space O(1)

 if not root: 
            return 0        # base case
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)



A new way i shall be doing this is solving on the website then hand writing it here instead of copy and pasting notes

Invert Binary Tree-

Second graph question, before watching the solution i thought DFS would work and struggled to implement BFS. However solution was way easier than i imagined.

inverseSelf(root)
if not root:
    return None

tmp = root.left
root.left = root.right
root.right = tmp

self.inverseSelf(root.left)
self.inverseSelf(root.right)

return root

isSameTree-

The bit I tripped up here was using  the recursion in the return and also using the and which makes a lot of sense but I was being silly and forgot

isSameTree(q-> treeNode, p->treeNode)
if not q and not p:
   return True
if not q or not p:
   return False
if q.val != p.val:
   return False

return self.isSameTree(q.right, p.right) and self.isSameTree(q.left, p.left)

Copy Linked List with Random Pointer

need to redo this, the concept of how we used the hash map was so weird but conceptually ok. Returning copyList[head] is also funky.

copyList(head):
 curr = head
 copyList = {None:None}

while curr:
   copy = Node(curr.val) //making the new nodes for copyList
   copyList[curr] = copy // making a hashmap mapping the current value with out new node
   curr = curr.next // next val

curr  = head

while curr:
   copy = copyList[curr]
   copy.next = copyList[curr.next] // Link the nodes together
   copy.random = copyList[curr.random] // linked the random vals together
   curr = curr.next// next curr

return copyList[head]

Unique Email Addresses

embarrassingly struggled with this one,  I know why im very bad at manipluating string so using .replace .split was a weak point. Mainly becuase I just didnt know the syntax and its just not built into my intuition

number of n bits:

Bit manipulation lowk be if you seen it you seen it.

numOfBit(n):

   res = 0 

 while n:

res += n % 2 // basically 1%2 =1, 0%2 =0

 n = n&gt;&gt; 1 // shift i place to the right for next num

return n

symmetricTree:

theres two places I mismanaged. The base case and the bfs inner function, makes sense though

def symmetricTree(self, root)
  def dfs(left,right)
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (right.val == left.val and dfs(left.left, right.right) and dfs(left.right, right.left))
    return dfs(root.left, root.right)

Diameter of Binary Tree

I dont get this and will have to revisit it when im in a better headspace.

