EXPAND_ALL_BUTTON = '//div[@class="rct-options"]/button[@aria-label="Expand all"]'
COLLAPSE_ALL_BUTTON = '//div[@class="rct-options"]/button[@aria-label="Collapse all"]'

TOGGLE_BUTTON = {
    'HOME_TOGGLE_BUTTON': '//button[@title="Toggle"][following::label[@for="tree-node-home"]]',
    'DESKTOP_TOGGLE_BUTTON': '//button[@title="Toggle"][following-sibling::label[@for="tree-node-desktop"]]',
    'DOCUMENTS_TOGGLE_BUTTON': '//button[@title="Toggle"][following-sibling::label[@for="tree-node-documents"]]',
    'WORKSPACE_TOGGLE_BUTTON': '//button[@title="Toggle"][following-sibling::label[@for="tree-node-workspace"]]',
    'OFFICE_TOGGLE_BUTTON': '//button[@title="Toggle"][following-sibling::label[@for="tree-node-office"]]',
    'DOWNLOADS_TOGGLE_BUTTON': '//button[@title="Toggle"][following-sibling::label[@for="tree-node-downloads"]]',
}

HOME_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-home"]]'
DESKTOP_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-desktop"]]'
NOTES_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-notes"]]'
COMMANDS_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-commands"]]'
DOCUMENTS_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-document"]]'
WORKSPACE_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-workspace"]]'
REACT_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-react"]]'
ANGULAR_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-angular"]]'
VEU_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-veu"]]'
PUBLIC_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-public"]]'
PRIVATE_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-private"]]'
CLASSIFIED_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-classified"]]'
GENERAL_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-general"]]'
DOWNLOADS_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-downloads"]]'
WORDFILE_DOC_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-wordFile"]]'
EXCELFILE_DOC_CHECKBOX = '//span[@class = "rct-checkbox"][ancestor::label[@for = "tree-node-excelFile"]]'


