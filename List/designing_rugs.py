def designing_rugs(height,width,sym):
    # res=[]
    # for i in range(height):
    #     row=width*sym
    #     res.append(row)
    #     print()
       
    # return res
    return [width*sym for i in range(height)]
output=designing_rugs(3,2,'#')
print(output, end=' ')
        
