import re

s = ' <div style="width:740px;overflow:hidden;height:30px;margin:0px auto;">\
<div id="PageList" style="width:20400px;"><a href="/index" class="pageCurrent">1</a>\
 <a href="/2.html" >2</a> <a href="/3.html" >3</a> <a href="/4.html" >4</a> <a href="/5.html"\
  >5</a> <a href="/6.html" >6</a> <a href="/7.html" >7</a> <a href="/8.html" >8</a> <a href="/9.\
  html" >9</a> <a href="/10.html" >10</a>  \
  <a href="javascript:void();" class="dotdot">..</a> <a href="/1275.html">1275</a> <a href="/2.html">&raquo;</a></div>    </div>'



div_pat = re.compile('class="dotdot".+?html">(.+?)</a>')
div = div_pat.search(s)
print(div.group())
print(div.group(1))
