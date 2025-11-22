from pyscript import document


# def calculateGWA(event):
#     sg_input = document.querySelector("#science_grade_input")
#     mg_input = document.querySelector("#math_grade_input")
#     eg_input = document.querySelector("#english_grade_input")
#     fg_input = document.querySelector("#filipino_grade_input")
#     ig_input = document.querySelector("#ict_grade_input")
#     pg_input = document.querySelector("#pe_grade_input")

#     sg = int(sg_input.value) 
#     mg = int(mg_input.value)
#     eg = int(eg_input.value)
#     fg = int(fg_input.value)
#     ig = int(ig_input.value)
#     pg = int(pg_input.value)

#     average = (float((sg + fg + mg + eg + fg + ig + pg)/5))

#     gwa_result_input = document.querySelector("#gwa_result")
#     gwa_result_input.innerHTML =  average

#     print(average)


# with loop hehe


def calculateGWA(event):

    inputIDS = [
        "#science_grade_input", 
        "#math_grade_input", 
        "#english_grade_input",
        "#filipino_grade_input",
        "#ict_grade_input",
        "#pe_grade_input"
    ]
    sum = 0

    for id in inputIDS:
        current_input = document.querySelector(id)
        print("for " + id)
        sum = sum + int(current_input.value)
    
    average =  float(sum / len(inputIDS))
    document.querySelector("#gwa_result").innerHTML = average

    print(average)


    