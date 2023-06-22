#Xpath
'''
1.XPath is defined as XMLpath.
2.it is a syntax or language for finding any element on the element on the webpage using XML path expression
3.xpath is used to find the location of any element on a webpage using HTML DOM structure.
4.Xpath can be used to navigate through element and attributes in DOm
5.Xpath is an address of the element
'''
#DOM-Document Object model
#   2type of XPATH
#1.Absolute/full XPATH   :::/html/body/nav/div/div[2]/div[1]/div/ul/li[2]/a/button
##/html/body/div/div[1]/div/div[1]/div/div[2]/div[1]/img

#2.Relative /partial XPATH ::://*[@id="navbarSupportedContent"]/div[1]/div/ul/li[2]/a/button

##//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[1]/img


 '''
DDifference Between Absolute xpath and Realtive Xpath
-----------------------------------------------------------
1.absolute xpath starts from root html node is None:
  .Relative xpath directly jump to element on DOM
2.absolute xpath we use only tags/node.
    .in Relative xpath we use attributes.
    
3.absolute xpath start with /
   .relative xpath starts with //
'''



 #how to write xpath manually
 #html/body/div[6]/div[1]/div[1]/div[2]/div[1]/u1/li[1]/a


 #syntax of writing relative xpath
 #  //tagname[@attribuste='value']
 #  //input[@id="small-searchterms"]
 #  //*[id="small-searchterms"]



 ##   Hoew to capture xpath automatically
#3.selectorHub



#Reason to prefer relative xpath
#1.if seveloper introduced new element than absolute xpath will be broken.
##    html/body/div[6]/div[1]/div[1]/div[2]/div[1]/u1/1i[1]/a
#2.if developer changed the location then absolute xpath will be broken

#absolute xpath is unstable





'''
1.Which xpath is prefered and why?
ans: Relative Xpath
xpath option
------------
1.and
2.or
3.contains()
4.startswith()
text()
'''

