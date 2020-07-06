def main():
        # Print testing because its  10minute challenge
        print("Test One")
        if same_necklace("nicole", "olenic"):
                print("Success")
        else:
                print("Fail")

        print("Test Two")
        if not same_necklace("nicole", "olenci"):
                print("Success")
        else:
                print("Fail")

        print("Challenge 2 Testing")
        sList = ["aaaaaaa", "abcabcabc", "a", ""]
        for s in sList:
                count = repeats(s)
                print(s + " repeats " + str(count) + " times")
	
def same_necklace(necklaceA, necklaceB):
	if len(necklaceA) != len(necklaceB):
		return False
	return necklaceA in necklaceB + necklaceB

def repeats(s):
        # I'd argue that "" repeats 0 times but the specification says it would return 1
        if s == "":
                 return 1
        repeats = 0
        sCopy = s
        for i in range(len(s)):
                if sCopy == (s[i:] + s[:i]):
                        repeats += 1
        return repeats
        

main()
