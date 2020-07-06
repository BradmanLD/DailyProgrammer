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
	
def same_necklace(necklaceA, necklaceB):
	if len(necklaceA) != len(necklaceB):
		return False
	return necklaceA in necklaceB + necklaceB


main()
