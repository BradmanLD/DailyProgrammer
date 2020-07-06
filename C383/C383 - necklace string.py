def main():
        if same_necklace("nicole", "olenic"):
                print("Success")
        else:
                print("Fail")
	
def same_necklace(necklaceA, necklaceB):
	if len(necklaceA) != len(necklaceB):
		return False
	return necklaceA in necklaceB + necklaceB


main()
