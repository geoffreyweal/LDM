"""
LDM.py, 22/10/2022, Geoffrey R. Weal

This program is designed to perform Literature data mining. This program is designed to

1. Scrap literature search websites like Google Scholar for literature.
2. Download the papers for those literatures as PDFs
3. Highlight relavant text in those PDFs

This program uses the `ScrapPaper` program that were originally developed by M. R. Rafsanjani. See https://github.com/rafsanlab/ScrapPaper and https://doi.org/10.1101/2022.03.08.483427

"""

import os, fitz

def highlight_pdf(filename, filepath, keywords):
	"""

	"""

	# First, open the PDf in fitz
	pdfIn = fitz.open(filepath+'/'+filename)

	# Second, highlight each page where keywords appear
	for page in pdfIn:

		text_instances = []
		for keyword in keywords:
			text_instances.append(page.search_for(keyword))
			text_instances.append(page.search_for(keyword.lower()))
			text_instances.append(page.search_for(keyword.upper()))
			text_instances.append(page.search_for(keyword.capitalize()))

		# iterate through each instance for highlighting
		for inst in text_instances:
			annot = page.add_highlight_annot(inst)
			# annot = page.add_rect_annot(inst)

			## Adding comment to the highlighted text
			info = annot.info
			info["title"] = "word_diffs"
			info["content"] = "diffs"
			annot.set_info(info)
			annot.update()

	# Third: Save the highlighted page.
	pdfIn.save(filepath+'/'+filename+'.tmp')

	# Fourth, remove the original pdf and replace it with the highlighted version.
	os.remove(filepath+'/'+filename)
	os.rename(filepath+'/'+filename+'.tmp', filepath+'/'+filename)