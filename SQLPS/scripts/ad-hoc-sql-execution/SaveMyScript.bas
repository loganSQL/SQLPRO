Attribute VB_Name = "Module1"
Public Sub SaveAttachmentsToDisk(MItem As Outlook.MailItem)
Dim oAttachment As Outlook.Attachment
Dim sSaveFolder As String
sSaveFolder = "C:\MyRequest\"
For Each oAttachment In MItem.Attachments
oAttachment.SaveAsFile sSaveFolder & oAttachment.DisplayName
Next
End Sub

Public Sub SaveAttachmentsToDiskRenameAsAdhoc(MItem As Outlook.MailItem)
Dim oAttachment As Outlook.Attachment
Dim sSaveFolder As String
Dim sAdhocPrefix As String
sSaveFolder = "C:\MyRequest\"
sAdhocPrefix = "Ad-Hoc-Script-" & Format(Now, "hh-mm-ss") & "-"
For Each oAttachment In MItem.Attachments
oAttachment.SaveAsFile sSaveFolder & sAdhocPrefix & oAttachment.DisplayName
Next
End Sub
