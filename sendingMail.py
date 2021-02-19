# importing the Yagmail library
import yagmail

the_text = """<p style="text-align: center;"><strong>D</strong><span>ata</span><strong> L</strong><span>ab</span><span> for </span><strong>A</strong><span>nnihilation</span><span>of </span><strong>C</strong><span>aste</span></p>
<p style="text-align: center;"><span>Secretariat, </span><strong>DLac</strong><strong>,<span> </strong><span>℅, Manuski, Deccan College Road, Yerwada, Pune 411006.&nbsp;</span></p>
<p style="text-align: center;"><a href="http://www.manuski.in/" target="_blank" rel="noopener noreferrer"><span>www.manuski.in</span></a><span>,&nbsp;</span><a href="mailto:info@manuski.in" rel="noreferrer"><span>dlac@manuski.in</span></a><span>, संपर्क ८९५६५७८७६३.&nbsp;</span></p>
<hr />
<p><span>Ref: PoA/FIR/2021/02/08 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>१८/०२/२०२१</span></p>
<p><span>जय भीम,</span></p>
<p><span>महाराष्ट्रात अनुसूचित जाती व अनुसूचित जमाती अत्याचार प्रतिबंधक कायद्यानुसार नोंदवल्या जाणाऱ्या तक्रारींची माहिती देण्याचा प्रयत्न आम्ही करत आहोत. या महिन्यात दिनांक १ जानेवारी ते ८ फेब्रुवारी २०२१ रोजी नोंद झालेल्या गुन्ह्यांचा सारांश व प्रथम खबरी अहवाल (FIR) च्या प्रति इमेल द्वारे बऱ्याच जनांपर्यंत पोचवण्याचा प्रयत्न करण्यात आला आहे. या मेल द्वारे ९ व १० फेब्रुवारी २०२१ रोजी महाराष्ट्रात अनुसूचित जाती आणि अनुसूचित जमाती अत्याचार प्रतिबंधक अधिनियम १९८९ अनुसार नोंद झालेल्या गुन्ह्यांचा सारांश खाली देण्यात येत आहे. सदर गुन्ह्यांच्या एफ.आय. आर. च्या प्रती सोबत जोडल्या आहेत. जातीय अत्याचाराने पीडित व्यक्तिंना योग्य तो कायदेशीर सल्ला व मानसिक पाठबळ मिळण्यासाठी यातून मदत व्हावी हि अपेक्षा. संविधानिक उद्देशांना गतिमान करण्याच्या हेतूने या माहितीचा कुठलीही संस्था किंवा व्यक्ती मुक्त वापर करून शकते. सदर उपयोग करताना डेटा लॅब (डी-लॅक) ने केलेल्या या प्रयत्नांचा उल्लेख करून योग्य ते श्रेयनिर्देश दिल्यास या प्रकल्पाला पाठबळ मिळेल याची कृपया नोंद घ्यावी. सदर माहितीत कुठलीही विसंगती आढळल्यास कृपया निदर्शनात आणून सहकार्य करावे.</span></p>
<p><strong>विशेष</strong><span>: सदर माहिती मध्ये केवळ नोंद झालेल्या व पोलिसांमार्फत संकेत स्थळावर उपलब्ध करण्यात आलेल्या <a href="https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx/robot.txt">(Maharashtra Police Published FIRs)</a> गुन्ह्यांचीची आकडेवारी दिली आहे. काही विशेष स्वरूपाच्या गुन्ह्यांची माहिती (उदाहरणार्थ लैंगिक अत्याचाराची प्रकरणे) अशा पद्धतीने संकेतस्थळावर न देण्याच्या विशेष सूचना आहेत. त्यानुसार हे गुन्हे संकेतस्थळावर उपलब्ध नाहीत व ते आकडेवारीत दिसत नाहीत. तसेच काही पोलिस स्टेशन त्यांच्याकडील नोंद गुन्ह्याच्या प्रति संकेत स्थळावर उपलब्ध करून देत नाहीत त्यामुळे त्यांचीही नोंद दिलेल्या आकडेवारी मध्ये नाही. </span></p>
<p><strong>दिनांक ०९ व १० फेब्रुवारी २०२१ रोजी महाराष्ट्रात अनुसूचित जाती आणि अनुसूचित जमाती अत्याचार प्रतिबंधक अधिनियम १९८९ नोंद झालेल्या तक्रारींचा सारांश:</strong></p>
<table style="background-color: #000000;" cellspacing="2">
<tbody>
<tr style="background-color: #bab6b6;">
<td>
<p><span>SN</span></p>
</td>
<td>
<p><strong>District</strong></p>
</td>
<td>
<p><strong>Police_Station</strong></p>
</td>
<td>
<p><strong>FIR</strong></p>
</td>
<td>
<p><strong>Date</strong></p>
</td>
<td>
<p><strong>Acts &amp; Sections</strong></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>1</span></p>
</td>
<td>
<p><span>AURANGABAD RURAL</span></p>
</td>
<td>
<p><span>PAITHAN</span></p>
</td>
<td>
<p><span>21</span></p>
</td>
<td>
<p><span>10/02/2021&nbsp;</span></p>
</td>
<td><p><span>भारतीय दंड संहिता १८६० - ३०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(2) </span></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>2</span></p>
</td>
<td>
<p><span>BEED</span></p>
</td>
<td>
<p><span>BEED CITY</span></p>
</td>
<td>
<p><span>23</span></p>
</td>
<td>
<p><span>09/02/2021&nbsp;</span></p>
</td>
<td>
<p><span>भारतीय दंड संहिता १८६० - १७७,१८२ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(p),3(1)(q) </span></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>3</span></p>
</td>
<td>
<p><span>BHANDARA</span></p>
</td>
<td>
<p><span>PALANDUR</span></p>
</td>
<td>
<p><span>09</span></p>
</td>
<td>
<p><span>10/02/2021</span></p>
</td>
<td>
<p><span>भारतीय दंड संहिता १८६० - २९४,३२३,३४,४२७,४५२ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s),3(1)(zb),3(2)(va)</span></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>4</span></p>
</td>
<td>
<p><span>NANDED</span></p>
</td>
<td>
<p><span>MUDKHED</span></p>
</td>
<td>
<p><span>32</span></p>
</td>
<td>
<p><span>10/02/2021</span></p>
</td>
<td>
<p><span>भारतीय दंड संहिता १८६० - ३२३,३४,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s) </span></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>5</span></p>
</td>
<td>
<p><span>NANDED</span></p>
</td>
<td>
<p><span>MUKHED</span></p>
</td>
<td>
<p><span>42</span></p>
</td>
<td>
<p><span>10/02/2021</span></p>
</td>
<td>
<p><span>भारतीय दंड संहिता १८६० - ३२३,३४,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(2)  </span></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>6</span></p>
</td>
<td>
<p><span>NASHIK RURAL</span></p>
</td>
<td>
<p><span>MALEGAON CHAWANI</span></p>
</td>
<td>
<p><span>40</span></p>
</td>
<td>
<p><span>10/02/2021</span></p>
</td>
<td>
<p><span>अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(u) </span></p>
</td>
</tr>

<tr style="background-color: #ffffff;">
<td>
<p><span>7</span></p>
</td>
<td>
<p><span>SATARA</span></p>
</td>
<td>
<p><span>PHALTAN RURAL</span></p>
</td>
<td>
<p><span>60</span></p>
</td>
<td>
<p><span>10/02/2021</span></p>
</td>
<td>
<p><span>अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(m),3(1)(r) </span></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>8</span></p>
</td>
<td>
<p><span>SOLAPUR RURAL</span></p>
</td>
<td>
<p><span>AKKALKOT NORTH</span></p>
</td>
<td>
<p><span>60</span></p>
</td>
<td>
<p><span>10/02/2021</span></p>
</td>
<td>
<p><span>भारतीय दंड संहिता १८६० - ३२३,३४,५०४,५०६ ; नागरी हक्‍क संरक्षण अधिनियम, १९५५ - 7(1)(d) ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s),3(2)(va) </span></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>9</span></p>
</td>
<td>
<p><span>SOLAPUR RURAL</span></p>
</td>
<td>
<p><span>VELAPUR</span></p>
</td>
<td>
<p><span>17</span></p>
</td>
<td>
<p><span>10/02/2021</span></p>
</td>
<td>
<p><span>भारतीय दंड संहिता १८६० - ५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(2)(va)  </span></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>10</span></p>
</td>
<td>
<p><span>THANE CITY</span></p>
</td>
<td>
<p><span>HILL LINE</span></p>
</td>
<td>
<p><span>26</span></p>
</td>
<td>
<p><span>09/02/2021</span></p>
</td>
<td>
<p><span>भारतीय दंड संहिता १८६० - ३२३,५०४ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s) </span></p>
</td>
</tr>
<tr style="background-color: #ffffff;">
<td>
<p><span>11</span></p>
</td>
<td>
<p><span>YAVATMAL</span></p>
</td>
<td>
<p><span>BABHULGAON</span></p>
</td>
<td>
<p><span>62</span></p>
</td>
<td>
<p><span>09/02/2021</span></p>
</td>
<td>
<p><span>भारतीय दंड संहिता १८६० - २९४,३२४,३३६,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्‍याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s),3(2)(va)  </span></p>
</td>
</tr>
</table>	
<p><span>वरील सारणी वरून हे स्पष्ट होते कि, दिनांक  ०९ व १० फेब्रुवारी २०२१ या काळात म्हणजेच २ दिवसांमध्ये, अनुसूचित जाती व अनुसूचित जमाती अत्याचार प्रतिबंधक कायदा १९८९ अनुसार कमीत कमी ११ गुन्हे नोंद झालेले आहेत. सोलापूर ग्रामीण व नांदेड या विभागात प्रत्येकी २ गुन्ह्यांची नोंद झालेली असून औरंगाबाद ग्रामीण, भंडारा, सातारा, नाशिक ग्रामीण, बीड, यवतमाळ व ठाणे शहर या जिल्ह्यांमध्ये प्रत्येकी एक गुन्ह्याची नोंद झाल्याचे दिसून येते.</span></p>
<p>डेटा टीम</p>
<p><span>संपर्क:</span></p>
<p><span>८९५६५७८७६३ /</span></p>
<p><span>८६५५५९९४३५/ ९९६७८८३९७३</span></p>"""

# initializing the server connection
yag = yagmail.SMTP({'dlac.automated@gmail.com': 'DO NOT REPLY'}, 'AB@ab@12')
# receiver list
receivers = ["sangharshbyss@gmail.com", "punjajikhandare1974@gmail.com",
             "kapilshivsharan37@gmail.com", "tribhuvanaseem@gmail.com",
             "shettyuttam@gmail.com", "esthappen90s@gmail.com", "anupriyavidrohi@gmail.com",
             "akashsable08@gmail.com", "vickynandgaye.mils@gmail.com",
             "somubaba123@gmail.com", "amolnimsadkar@gmail.com", "mind.ravi@gmail.com",
             "dh.vivekmitra@gmail.com", "vipulk2703@gmail.com", "vinod.shinde124@gmail.com",
             "varshat375@gmail.com", "sachinujgare@gmail.com", "aashishsonawane02@gmail.com",
             "vickypatild@gmail.com", "pghunnar@gmail.com", "sawansomwanshi@gmail.com",
             "jayeshkedare@gmail.com", "anu.salelkar@gmail.com", "bhanubaudh@gmail.com",
             "maitreyaratna@gmail.com", "manjula.hp@gmail.com", "maitreya.hyaling@gmail.com",
             "maitreyayogesh@gmail.com", "prachi06salve@gmail.com", "aniket.khadse@gmail.com",
             "p.m.rangari@gmail.com", "dycomcvcmumbaicity@gmail.com", "sheela.mangesh@gmail.com",
             "sheela.mangesh@gmail.com", "shakyaslegals@gmail.com", "prathmesh.news@gmail.com",
             "sukanya.shantha@gmail.com", "vishal.thakare09@gmail.com", "apeksha.jadhao1987@gmail.com",
             "tiss.pranay@gmail.com", "adv.kavitanw@gmail.com", "bysskishor@gmail.com",
             "vikramsonde@gmail.com", "amittikhade11@gmail.com", "adv.ambadasbansode@gmail.com",
             "sharad.shelke@gmail.com", "a1prashant@yahoo.com",
             "vaishupiyu14feb@gmail.com", "Shantikamal2217@gmail.com", "sachinkamble30@gmail.com",
             "ravindracw@gmail.com", "mind.ravi@gmail.com", "usabhi.milind@gmail.com",
             "sgedam40@yahoo.com", "disha.kad@gmail.com", "maitreyanath@gmail.com",
             "vishalsarpe09@gmail.com", "kambledipankar10@gmail.com", "mapu.zagade@gmail.com",
             "sandip.hire001@gmail.com", "chandanshive.aditya@gmail.com", "pradnyasuryashende@gmail.com",
             "vijaynag10@gmail.com", "milindkshir@gmail.com", "waghchaurejay@gmail.com",
             "ashwajit77@gmail.com", "rupali21213@gmail.com", "surendra.bhalerao@gmail.com",
             "adsujit.tiss@gmail.com", "bsravi.b@gmail.com", "asmita.tiss2012@gmail.com",
             "baudhswati@gmail.com", "vishwajit.vinay@gmail.com", "bansode.maya156@gmail.com",
             "ndhaktode@gmail.com", "priyajmsw@gmail.com", "kthorat39@gmail.com",
             "minalsangole1801@gmail.com", "namrata.lokhande63@gmail.com",
             "mekalesantosh@gmail.com", "sbtt.1119@gmail.com", "rrupesh88@gmail.com",
             "sneha.magar1992@gmail.com", "vanitatumsare@gmail.com", "uttam.madane@gmail.com",
             "sreejithmanu@gmail.com", "ambhore.766266@gmail.com", "aniltharayath@gmail.com",
             "sorenlakhindar@gmail.com", "sawantsuresh@gmail.com", "sumedhsgondane@gmail.com",
             "vivekbansode81@gmail.com", "shreyaskamble95@gmail.com", "preranadhende3@gmail.com",
             "yogothegreat@gmail.com", "vijay_sonkamble@yahoo.com", "atultiss2010@gmail.com",
             "dranilsapkal@gmail.com", "vishugaikwad1985@gmail.com", "sudeshpawar98@gmail.com",
             "sangramsavant2782@gmail.com", "satishsampada@gmail.com", "kambleashish300@mail.com",
             "sheetal28kamble@gmail.com"]
# sending the email
for name in receivers:
    yag.send(to=name,
             subject='(Marathi) 09-10 February 2021 PoA Update: Complaints registered ',
             contents=the_text,
             attachments=['/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen.pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(1).pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(2).pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(3).pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(4).pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(5).pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(6).pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(7).pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(8).pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(9).pdf',
                          '/home/sangharsh/Documents/PoA/data/FIR/February/copies/09022021 '
                          '_ 10022021/rptFIR_Publish_Citizen(10).pdf'
                          ])

print(f'Email successfully sent to {len(receivers) } participants')
