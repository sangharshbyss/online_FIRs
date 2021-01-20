#importing the Yagmail library
import yagmail
import content_text

html = """<p>
    <meta charset="utf-8">
</p>
<div align="left" dir="ltr" style="margin-left:0pt;">
    <table style="border:none;border-collapse:collapse;">
        <tbody>
            <tr style="height:21pt;">
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">SN</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:middle;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">District</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:middle;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Police_Station</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:middle;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">FIR</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:middle;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Date</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:middle;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Acts_&amp;_Sections</span></p>
                </td>
            </tr>
            <tr style="height:21pt;">
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">1</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">AURANGABAD RURAL</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">VAIJAPUR</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">21</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">13/01/2021&nbsp;</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">भारतीय दंड संहिता १८६० - ३२३,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s) ;</span></p>
                </td>
            </tr>
            <tr style="height:21pt;">
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">2</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">SOLAPUR RURAL</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">PANDHARPUR TALUKA</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">32</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">13/01/2021&nbsp;</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">भारतीय दंड संहिता १८६० - १४३,१४७,१४८,१४९,३२३,३२६,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s) ; महाराष्ट्र पोलीस अधिनियम, १९५१ - 135 ;</span></p>
                </td>
            </tr>
            <tr style="height:21pt;">
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">3</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">SOLAPUR RURAL</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">SOLAPUR</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">44</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">13/01/2021</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">भारतीय दंड संहिता १८६० - १४३,१४७,१४८,३२३,३२६,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s),3(2)(va) ;</span></p>
                </td>
            </tr>
            <tr style="height:21pt;">
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">4</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">THANE CITY</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">NAUPADA</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">11</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">13/01/2021</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">भारतीय दंड संहिता १८६० - ३२३,३४,४०६,४२०,४६५,४६७,४६८,४७१,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3,3(1)(r),3(1)(s) ;</span></p>
                </td>
            </tr>
            <tr style="height:21pt;">
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">5</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">NAVI MUMBAI</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">NAVIN PANVEL</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">13</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">14/01/2021</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">भारतीय दंड संहिता १८६० - १०९,३२३,३४१,५०४,५०६ ; नागरी हक्&zwj;क संरक्षण अधिनियम, १९५५ - 7(1)(d),7(1-A) ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(p),3(1)(q),3(1)(r),3(1)(za)(A),3(1)(zc),3(2)(va),३(२)(दोन),३(२)(पाच) ;</span></p>
                </td>
            </tr>
            <tr style="height:21pt;">
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">6</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">SOLAPUR RURAL</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">MALSHIRAS</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">28</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">14/01/2021</span></p>
                </td>
                <td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:bottom;background-color:#ffffff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;">
                    <p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">भारतीय दंड संहिता १८६० - ३४,३४१,५०४,५०६ ; नागरी हक्&zwj;क संरक्षण अधिनियम, १९५५ - 7(1)(d) ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s),3(1)(y),3(2)(va) ;</span></p>
                </td>
            </tr>
        </tbody>
    </table>
</div>"""

text1 = """<p>
    <meta charset="utf-8">
</p>
<p dir="ltr" style="line-height:1.38;text-align: right;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">१९/०१/२०२१</span></p>
<p dir="ltr" style="line-height:1.38;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">जय भीम,</span></p>
<p><br></p>
<p dir="ltr" style="line-height:1.38;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">दिनांक १ जानेवारी ते दिनांक १२ जानेवारी २०२१ या काळात महाराष्ट्रात नोंद झालेल्या गुन्ह्यांचा सारांश व प्रथम खबरी अहवाल (FIR) च्या प्रति इमेल द्वारे बऱ्याच जनांपर्यंत पोचवण्याचा प्रयत्न करण्यात आला. आता १३ जानेवारी ते १५ जानेवारी २०२१ पर्यंत महाराष्ट्रात अनुसूचित जाती आणि अनुसूचित जमाती अत्याचार प्रतिबंधक अधिनियम १९८९ अनुसार नोंद झालेल्या गुन्ह्यांचा सारांश खाली देण्यात येत आहे. सदर गुन्ह्यांच्या एफ.आय. आर. च्या प्रती सोबत जोडल्या आहेत. जातीय अत्याचाराने पीडित व्यक्तिंना योग्य तो कायदेशीर सल्ला &nbsp;व मानसिक पाठबळ मिळण्यासाठी यातून मदत व्हावी हि अपेक्षा. संविधानिक उद्देशांना गतिमान करण्याच्या हेतूने या माहितीचा कुठलीही संस्था किंवा व्यक्ती मुक्त वापर करून शकते. सदर उपयोग करताना डेटा लॅब (डी-लॅक) ने केलेल्या या प्रयत्नांचा उल्लेख करून योग्य ते श्रेयनिर्देश दिल्यास या प्रकल्पाला पाठबळ मिळेल याची कृपया नोंद घ्यावी. सदर माहितीत &nbsp;कुठलीही विसंगती आढळल्यास कृपया निदर्शनात आणून सहकार्य करावे.&nbsp;</span></p>
<p><br></p>
<p><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">विशेष</span><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">: &nbsp;सदर माहिती मध्ये केवळ नोंद झालेल्या व पोलिसांमार्फत संकेत स्थळावर उपलब्ध करण्यात आलेल्या गुन्ह्यांचीची आकडेवारी दिली आहे. काही विशेष स्वरूपाच्या गुन्ह्यांची माहिती (उदाहरणार्थ लैंगिक अत्याचाराची प्रकरणे) अशा पद्धतीने संकेतस्थळावर न देण्याच्या विशेष सूचना आहेत. त्यानुसार हे गुन्हे संकेतस्थळावर उपलब्ध नाहीत व ते आकडेवारीत दिसत नाहीत. तसेच काही पोलिस स्टेशन त्यांच्याकडील &nbsp;नोंद गुन्ह्याच्या प्रति संकेत स्थळावर उपलब्ध करून देत नाहीत त्यामुळे त्यांचीही नोंद दिलेल्या आकडेवारी मध्ये नाही. दिनांक १३ जानेवारी ते १५ जानेवारी २०२१ याकाळात महाराष्ट्रात अनुसूचित जाती आणि अनुसूचित जमाती अत्याचार प्रतिबंधक अधिनियम १९८९ नोंद झालेल्या तक्रारींचा सारांश:&nbsp;</span></p>"""

text2 = """<p>
    <meta charset="utf-8">
</p>
<p dir="ltr" style="line-height:1.38;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">वरील सारणी वरून हे स्पष्ट होते कि, दिनांक १३ जानेवारी ते दिनांक १५ जानेवारी २०२१ या काळात म्हणजेच ३ दिवसांमध्ये, अनुसूचित जाती व अनुसूचित जमाती अत्याचार प्रतिबंधक कायदा १९८९ अनुसार कमीत कमी ६ गुन्हे नोंद झालेले आहेत. यापैकी सोलापूर ग्रामीण या विभागात ३ गुन्ह्यांची नोंद झाल्याचे दिसून येते. तसेच ठाणे शहर, नवी मुंबई व औरंगाबाद ग्रामीण या ठिकाणी या जिल्ह्यांमध्ये प्रत्येकी एक गुन्ह्याची नोंद झाल्याचे दिसून येते. &nbsp;</span></p>
<p><br></p>
<p dir="ltr" style="line-height:1.38;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">डेटा &nbsp;टीम&nbsp;</span></p>
<p dir="ltr" style="line-height:1.38;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">संपर्क:&nbsp;</span></p>
<p dir="ltr" style="line-height:1.38;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">८६५५५९९४३५/ ९९६७८८३९७३</span></p>"""

text_head = """<p>
    <meta charset="utf-8">
</p>
<p dir="ltr" style="line-height:1.2;margin-left: -21.259842519685044pt;margin-right: -30.389763779527556pt;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:30pt;font-family:Audiowide,cursive;color:#000000;background-color:#ffffff;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">D</span><span style="font-size:30pt;font-family:Audiowide,cursive;color:#3d85c6;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">ata</span><span style="font-size:30pt;font-family:Audiowide,cursive;color:#000000;background-color:#ffffff;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;L</span><span style="font-size:30pt;font-family:Audiowide,cursive;color:#3d85c6;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">ab</span><span style="font-size:30pt;font-family:'Black Ops One',cursive;color:#000000;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;</span><span style="font-size:18pt;font-family:Arial;color:#000000;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">for</span><span style="font-size:22pt;font-family:Arial;color:#000000;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;</span><span style="font-size:27.999999999999996pt;font-family:Merriweather,serif;color:#000000;background-color:#ffffff;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">A</span><span style="font-size:27.999999999999996pt;font-family:Merriweather,serif;color:#3d85c6;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">nnihilation</span><span style="font-size:27.999999999999996pt;font-family:Merriweather,serif;color:#000000;background-color:#ffffff;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;</span><span style="font-size:18pt;font-family:Merriweather,serif;color:#000000;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">of</span><span style="font-size:27.999999999999996pt;font-family:Merriweather,serif;color:#000000;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;</span><span style="font-size:27.999999999999996pt;font-family:Merriweather,serif;color:#000000;background-color:#ffffff;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">C</span><span style="font-size:27.999999999999996pt;font-family:Merriweather,serif;color:#3d85c6;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">aste</span><span style="font-size:27.999999999999996pt;font-family:'Black Ops One',cursive;color:#0b5394;background-color:#ffffff;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;</span></p>
<p dir="ltr" style="line-height:1.2;margin-left: -28.346456692913385pt;margin-right: -30.389763779527556pt;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Secretariat,&nbsp;</span><span style="font-size:16pt;font-family:Audiowide,cursive;color:#3d85c6;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">DLac</span><span style="font-size:12pt;font-family:Arial;color:#3c78d8;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">,&nbsp;</span><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">℅, Manuski, Deccan College Road, Yerwada, Pune 411006.&nbsp;</span></p>
<p dir="ltr" style="line-height:1.2;margin-left: -28.346456692913385pt;margin-right: -30.389763779527556pt;text-align: center;margin-top:0pt;margin-bottom:0pt;"><a href="http://www.manuski.org" style="text-decoration:none;"><span style="font-size:12pt;font-family:Arial;color:#1155cc;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:underline;-webkit-text-decoration-skip:none;text-decoration-skip-ink:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">www.manuski.org</span></a><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">,&nbsp;</span><a href="mailto:info@manuski.org" style="text-decoration:none;"><span style="font-size:12pt;font-family:Arial;color:#1155cc;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:underline;-webkit-text-decoration-skip:none;text-decoration-skip-ink:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">info@manuski.org</span></a><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">, +91 9967883973.&nbsp;</span></p>
<p dir="ltr" style="line-height:1.38;margin-left: -28.346456692913385pt;margin-right: -30.389763779527556pt;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><img src="https://docs.google.com/drawings/u/0/d/syBQh3pJTyqy8_S7wuptvBw/image?w=602&h=3&rev=1&ac=1&parent=11HtoqtRsc56m7lzMF5P_hTrgQlgmu5O_wHXeH1X5wY8" style="border: medium none;" width="602" height="3"></span></p>
<p dir="ltr" style="line-height:1.38;margin-left: -28.346456692913385pt;margin-right: -30.389763779527556pt;text-indent: 28.346456692913385pt;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:9pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Ref: PoA/FIR/2021/01/03</span></p>
<p><br></p>
<p><br></p>"""
all_html = """<h1 style="text-align: center;"><strong>Data Lab for Annihilation of Caste&nbsp;</strong></h1>
<p style="text-align: center;"><span style="font-weight: 400;">Secretariat, </span><strong>DLac</strong><strong>, </strong><span style="font-weight: 400;">℅, Manuski, Deccan College Road, Yerwada, Pune 411006.&nbsp;</span></p>
<p style="text-align: center;"><a href="http://www.manuski.org"><span style="font-weight: 400;">www.manuski.org</span></a><span style="font-weight: 400;">, </span><a href="mailto:info@manuski.org"><span style="font-weight: 400;">info@manuski.org</span></a><span style="font-weight: 400;">, +91 9967883973.&nbsp;</span></p>
<p><span style="font-weight: 400;">Ref: PoA/FIR/2021/01/03</span></p>
<p style="text-align: right;"><span style="font-weight: 400;">१९/०१/२०२१</span></p>
<p><span style="font-weight: 400;">जय भीम,</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">दिनांक १ जानेवारी ते दिनांक १२ जानेवारी २०२१ या काळात महाराष्ट्रात नोंद झालेल्या गुन्ह्यांचा सारांश व प्रथम खबरी अहवाल (FIR) च्या प्रति इमेल द्वारे बऱ्याच जनांपर्यंत पोचवण्याचा प्रयत्न करण्यात आला. आता १३ जानेवारी ते १५ जानेवारी २०२१ पर्यंत महाराष्ट्रात अनुसूचित जाती आणि अनुसूचित जमाती अत्याचार प्रतिबंधक अधिनियम १९८९ अनुसार नोंद झालेल्या गुन्ह्यांचा सारांश खाली देण्यात येत आहे. सदर गुन्ह्यांच्या एफ.आय. आर. च्या प्रती सोबत जोडल्या आहेत. जातीय अत्याचाराने पीडित व्यक्तिंना योग्य तो कायदेशीर सल्ला&nbsp; व मानसिक पाठबळ मिळण्यासाठी यातून मदत व्हावी हि अपेक्षा. संविधानिक उद्देशांना गतिमान करण्याच्या हेतूने या माहितीचा कुठलीही संस्था किंवा व्यक्ती मुक्त वापर करून शकते. सदर उपयोग करताना डेटा लॅब (डी-लॅक) ने केलेल्या या प्रयत्नांचा उल्लेख करून योग्य ते श्रेयनिर्देश दिल्यास या प्रकल्पाला पाठबळ मिळेल याची कृपया नोंद घ्यावी. सदर माहितीत&nbsp; कुठलीही विसंगती आढळल्यास कृपया निदर्शनात आणून सहकार्य करावे.&nbsp;</span></p>
<p>&nbsp;</p>
<p><strong>विशेष</strong><span style="font-weight: 400;">:&nbsp; सदर माहिती मध्ये केवळ नोंद झालेल्या व पोलिसांमार्फत संकेत स्थळावर उपलब्ध करण्यात आलेल्या गुन्ह्यांचीची आकडेवारी दिली आहे. काही विशेष स्वरूपाच्या गुन्ह्यांची माहिती (उदाहरणार्थ लैंगिक अत्याचाराची प्रकरणे) अशा पद्धतीने संकेतस्थळावर न देण्याच्या विशेष सूचना आहेत. त्यानुसार हे गुन्हे संकेतस्थळावर उपलब्ध नाहीत व ते आकडेवारीत दिसत नाहीत. तसेच काही पोलिस स्टेशन त्यांच्याकडील&nbsp; नोंद गुन्ह्याच्या प्रति संकेत स्थळावर उपलब्ध करून देत नाहीत त्यामुळे त्यांचीही नोंद दिलेल्या आकडेवारी मध्ये नाही.&nbsp;</span></p>
<p>&nbsp;</p>
<p><strong>दिनांक १३ जानेवारी ते १५ जानेवारी २०२१ याकाळात महाराष्ट्रात अनुसूचित जाती आणि अनुसूचित जमाती अत्याचार प्रतिबंधक अधिनियम १९८९ नोंद झालेल्या तक्रारींचा सारांश:</strong></p>
<p>&nbsp;</p>
<table style="width: 1030px; background-color: #ecf4f5; margin-left: auto; margin-right: auto;" border="1" cellpadding="1"><caption>&nbsp;</caption>
<tbody>
<tr style="height: 35px; background-color: #f9fab7;">
<td style="width: 15px; height: 35px; text-align: center;">
<p><strong>SN</strong></p>
</td>
<td style="width: 97.2333px; height: 35px; text-align: center;">
<p><strong>District</strong></p>
</td>
<td style="width: 97.7667px; height: 35px; text-align: center;">
<p><strong>Police_Station</strong></p>
</td>
<td style="width: 17px; height: 35px; text-align: center;">
<p><strong>FIR</strong></p>
</td>
<td style="width: 58px; height: 35px; text-align: center;">
<p><strong>Date</strong></p>
</td>
<td style="width: 702px; height: 35px; text-align: center;">
<p><strong>Acts_&amp;_Sections</strong></p>
</td>
</tr>
<tr style="height: 48.4667px; background-color: #aad8f1;">
<td style="width: 15px; height: 48.4667px;">
<p><span style="font-weight: 400;">1</span></p>
</td>
<td style="width: 97.2333px; height: 48.4667px;">
<p><span style="font-weight: 400;">AURANGABAD RURAL</span></p>
</td>
<td style="width: 97.7667px; height: 48.4667px;">
<p><span style="font-weight: 400;">VAIJAPUR</span></p>
</td>
<td style="width: 17px; height: 48.4667px;">
<p><span style="font-weight: 400;">21</span></p>
</td>
<td style="width: 58px; height: 48.4667px;">
<p><span style="font-weight: 400;">13/01/2021&nbsp;</span></p>
</td>
<td style="width: 702px; height: 48.4667px;">
<p><span style="font-weight: 400;">भारतीय दंड संहिता १८६० - ३२३,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s) ;</span></p>
</td>
</tr>
<tr style="height: 52px;">
<td style="width: 15px; height: 52px;">
<p><span style="font-weight: 400;">2</span></p>
</td>
<td style="width: 97.2333px; height: 52px;">
<p><span style="font-weight: 400;">SOLAPUR RURAL</span></p>
</td>
<td style="width: 97.7667px; height: 52px;">
<p><span style="font-weight: 400;">PANDHARPUR TALUKA</span></p>
</td>
<td style="width: 17px; height: 52px;">
<p><span style="font-weight: 400;">32</span></p>
</td>
<td style="width: 58px; height: 52px;">
<p><span style="font-weight: 400;">13/01/2021&nbsp;</span></p>
</td>
<td style="width: 702px; height: 52px;">
<p><span style="font-weight: 400;">भारतीय दंड संहिता १८६० - १४३,१४७,१४८,१४९,३२३,३२६,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s) ; महाराष्ट्र पोलीस अधिनियम, १९५१ - 135 ;</span></p>
</td>
</tr>
<tr style="height: 50px; background-color: #aad8f1;">
<td style="width: 15px; height: 50px;">
<p><span style="font-weight: 400;">3</span></p>
</td>
<td style="width: 97.2333px; height: 50px;">
<p><span style="font-weight: 400;">SOLAPUR RURAL</span></p>
</td>
<td style="width: 97.7667px; height: 50px;">
<p><span style="font-weight: 400;">SOLAPUR</span></p>
</td>
<td style="width: 17px; height: 50px;">
<p><span style="font-weight: 400;">44</span></p>
</td>
<td style="width: 58px; height: 50px;">
<p><span style="font-weight: 400;">13/01/2021</span></p>
</td>
<td style="width: 702px; height: 50px;">
<p><span style="font-weight: 400;">भारतीय दंड संहिता १८६० - १४३,१४७,१४८,३२३,३२६,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s),3(2)(va) ;</span></p>
</td>
</tr>
<tr style="height: 50px;">
<td style="width: 15px; height: 50px;">
<p><span style="font-weight: 400;">4</span></p>
</td>
<td style="width: 97.2333px; height: 50px;">
<p><span style="font-weight: 400;">THANE CITY</span></p>
</td>
<td style="width: 97.7667px; height: 50px;">
<p><span style="font-weight: 400;">NAUPADA</span></p>
</td>
<td style="width: 17px; height: 50px;">
<p><span style="font-weight: 400;">11</span></p>
</td>
<td style="width: 58px; height: 50px;">
<p><span style="font-weight: 400;">13/01/2021</span></p>
</td>
<td style="width: 702px; height: 50px;">
<p><span style="font-weight: 400;">भारतीय दंड संहिता १८६० - ३२३,३४,४०६,४२०,४६५,४६७,४६८,४७१,५०४,५०६ ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3,3(1)(r),3(1)(s) ;</span></p>
</td>
</tr>
<tr style="height: 52px; background-color: #aad8f1;">
<td style="width: 15px; height: 52px;">
<p><span style="font-weight: 400;">5</span></p>
</td>
<td style="width: 97.2333px; height: 52px;">
<p><span style="font-weight: 400;">NAVI MUMBAI</span></p>
</td>
<td style="width: 97.7667px; height: 52px;">
<p><span style="font-weight: 400;">NAVIN PANVEL</span></p>
</td>
<td style="width: 17px; height: 52px;">
<p><span style="font-weight: 400;">13</span></p>
</td>
<td style="width: 58px; height: 52px;">
<p><span style="font-weight: 400;">14/01/2021</span></p>
</td>
<td style="width: 702px; height: 52px;">
<p><span style="font-weight: 400;">भारतीय दंड संहिता १८६० - १०९,३२३,३४१,५०४,५०६ ; नागरी हक्&zwj;क संरक्षण अधिनियम, १९५५ - 7(1)(d),7(1-A) ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(p),3(1)(q),3(1)(r),3(1)(za)(A),3(1)(zc),3(2)(va),३(२)(दोन),३(२)(पाच) ;</span></p>
</td>
</tr>
<tr style="height: 52px;">
<td style="width: 15px; height: 52px;">
<p><span style="font-weight: 400;">6</span></p>
</td>
<td style="width: 97.2333px; height: 52px;">
<p><span style="font-weight: 400;">SOLAPUR RURAL</span></p>
</td>
<td style="width: 97.7667px; height: 52px;">
<p><span style="font-weight: 400;">MALSHIRAS</span></p>
</td>
<td style="width: 17px; height: 52px;">
<p><span style="font-weight: 400;">28</span></p>
</td>
<td style="width: 58px; height: 52px;">
<p><span style="font-weight: 400;">14/01/2021</span></p>
</td>
<td style="width: 702px; height: 52px;">
<p><span style="font-weight: 400;">भारतीय दंड संहिता १८६० - ३४,३४१,५०४,५०६ ; नागरी हक्&zwj;क संरक्षण अधिनियम, १९५५ - 7(1)(d) ; अनुसूचीत जाती आणि अनुसूचीत जमाती (अत्&zwj;याचार प्रतिबंधक) अधिनियम, १९८९ - 3(1)(r),3(1)(s),3(1)(y),3(2)(va) ;</span></p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">वरील सारणी वरून हे स्पष्ट होते कि, दिनांक १३ जानेवारी ते दिनांक १५ जानेवारी २०२१ या काळात म्हणजेच ३ दिवसांमध्ये, अनुसूचित जाती व अनुसूचित जमाती अत्याचार प्रतिबंधक कायदा १९८९ अनुसार कमीत कमी ६ गुन्हे नोंद झालेले आहेत. यापैकी सोलापूर ग्रामीण या विभागात ३ गुन्ह्यांची नोंद झाल्याचे दिसून येते. तसेच ठाणे शहर, नवी मुंबई व औरंगाबाद ग्रामीण या ठिकाणी या जिल्ह्यांमध्ये प्रत्येकी एक गुन्ह्याची नोंद झाल्याचे दिसून येते.&nbsp;&nbsp;</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">डेटा&nbsp; टीम&nbsp;</span></p>
<p><span style="font-weight: 400;">संपर्क:&nbsp;</span></p>
<p>8956578763 / 8655599435</p>"""

#initializing the server connection
yag = yagmail.SMTP(user='dlac.automated@gmail.com', password='AB@ab@12')
#sending the email
yag.send(to='sorenlakhindar@gmail.com',
         subject='Testing Atuomation. Ignore',
         contents= all_html,
         attachments = '/home/sangharsh/Documents/PoA/data/FIR/' \
                      'January/copies/14012021 _ 14012021/' \
                      'rptFIR_Publish_Citizen(5).pdf')
print("Email sent successfully")

