def main():
    score = int(input("Score: "))
    message = "Grade: "
    if score >= 90:
        message+="A"
    elif score >= 80:
        message+="B"
    elif score >= 70:
        message+= "C"
    elif score >= 60:
        message+= "D"
    else:
        message+= "F"
    
    print(message)

main()
