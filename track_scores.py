def track_scores(scores,operations):
    operations=str(input("enter an operation(max, sum, even):"))
    if operations=="sum":
        sum=scores[0]+scores[1]+scores[2]+scores[3]+scores[4]
        print(sum)
    elif operations=="max":
            if scores[0]>scores[1]>scores[2]>scores[3]>scores[4]:
                print(f"max={scores[0]}")
            elif scores[1]>scores[2]>scores[3]>scores[4]>scores[0]:
                print(f"max={scores[1]}")
            elif scores[2]>scores[3]>scores[4]>scores[0]>scores[1]:
                print(f"max={scores[2]}")
            elif scores[3]>scores[4]>scores[0]>scores[1]>scores[2]:
                print(f"max={scores[3]}")
            else:
                print(f"max={scores[4]}")
    elif operations=="even":
            for score in scores:
                 if score%2==0:
                      print(score)
                      score=score+1
    else:
         print("invalid operation:,)")

track_scores((53,72,90,110,130),"operations")