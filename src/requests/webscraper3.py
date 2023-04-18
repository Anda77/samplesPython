from bs4 import BeautifulSoup
from lxml import etree

html_doc = """
<html>
<head>
</head>
<body>
   <div class="container">
      <section id="page">
         <div class="content">   
            <div class="box">  
               <ul>
                  <li>Name: Peter</li>
                  <li>Age: 21</li>
                  <li>Status: Active</li>
               </ul> 
            </div>
         </div>
      </section>
   </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
dom = etree.HTML(str(soup))
for li in dom.xpath('/html/body/div/section/div[1]/div[1]/ul/li[3]/text()'):
    txt = li.split()[1]
    print(txt)
