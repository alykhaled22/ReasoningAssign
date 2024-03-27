def eliminate_implication(expression):
    if "=>" in expression:
        subS = expression.split("=>")
        return f"(~{subS[0].strip()} | {subS[1].strip()})"


def move_negation_inward(expression):
    negation = False
    Fexp = ""
    indoor = False
    for char in expression:

        if char == "~" and indoor:
            Fexp += char

        elif char == "~" and not negation:
            negation = True

        elif char == "|":
            Fexp += "&" if negation else "|"

        elif char == "&":
            Fexp += "|" if negation else "&"

        elif char == "(" and negation:
            indoor = True
            Fexp += char

        elif char == "(" and not negation:
            indoor = True
            Fexp += char

        elif char == ")" and negation:
            Fexp += char
            negation = False
            indoor = False

        elif char == " ":
            Fexp += char

        else:
            Fexp += "~" if negation else ""
            Fexp += char
    return Fexp


test = move_negation_inward("~(~q & ~p)")
print(test)


def RemovedoubleNot(expression):
    Fexp = ""
    cnt = 0
    for char in expression:

        if char == "~":
            cnt += 1
       
        else:
            if cnt % 2 != 0 and cnt != 0:
                Fexp += "~"
            Fexp += char
            cnt = 0

    return Fexp


print(RemovedoubleNot(test))


def Standardizevariables(expression):
    Fexp = ""
    sympols = []
    ch = ""
    operations = ["|", "&", "="]
    replace = False

    for char in expression:

        if char in sympols and replace:
            ch = chr(ord(sympols[-1]) + 1)
            Fexp += ch

        else:
            if ord(char) >= 97 and ord(char) <= 122:
                sympols.append(char)
                replace = False

            else:
                if char in operations:
                    replace = True
                
                elif char == ")":
                    replace = False
                    if ch != "":
                        sympols.append(ch)
            Fexp += char
    return Fexp


test2 = "(∀x P(x)) | (∃x Q(x)) => (∃z Q(z))"
print(Standardizevariables(test2))


def ThePrenexForm(expression):
    Fexp = ""
    subS = " "

    for char in expression:
        
        if char == "∀" or char == "∃":
            subS += char

        elif subS[-1] == "∃" or subS[-1] == "∀":
            subS += char + " "
        elif char ==' ' and Fexp[-1] == '(':
            continue
        else:
            Fexp += char

    Fexp = subS.strip()+ ' ' + Fexp
    print(Fexp)


ThePrenexForm(test2)

 def skolemize(expression):
       i=0
       count=1
       while i<len(expression):
        if expression [i]==  ='∃':
            last_universal= expression[:i].rfind('∀')
            if last_universal =-1
            expression=expression[:i]+expression[i+2:] replace(expression[i+1], , 'f'+str(count)+'('+expression[last_universal+1]+')'
            )count+=1
            else :
                i+= 1
                return expression
            

            def eliminate_univarsel_quantifiers(expression):

