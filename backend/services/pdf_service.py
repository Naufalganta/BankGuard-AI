from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class PDFService:

    @staticmethod
    def generate(filename, result):

        pdf_name = f"reports/{filename}.pdf"

        doc = SimpleDocTemplate(pdf_name)

        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("<b>BankGuard AI Report</b>", styles["Title"]))

        story.append(
            Paragraph(
                f"<b>File:</b> {filename}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Risk:</b> {result['risk']}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Summary:</b><br/>{result['summary']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                "<b>Threat:</b>",
                styles["Heading2"]
            )
        )

        for item in result["threat"]:
            story.append(
                Paragraph(f"• {item}", styles["Normal"])
            )

        story.append(
            Paragraph(
                "<b>Evidence:</b>",
                styles["Heading2"]
            )
        )

        for item in result["evidence"]:
            story.append(
                Paragraph(f"• {item}", styles["Normal"])
            )

        story.append(
            Paragraph(
                "<b>Recommendation:</b>",
                styles["Heading2"]
            )
        )

        for item in result["recommendation"]:
            story.append(
                Paragraph(f"• {item}", styles["Normal"])
            )

        doc.build(story)

        return pdf_name