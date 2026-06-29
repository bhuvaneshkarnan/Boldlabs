// EmailJS configuration keys (Replace with your actual EmailJS credentials)
const emailjsConfig = {
  publicKey: "YOUR_EMAILJS_PUBLIC_KEY",
  serviceId: "YOUR_EMAILJS_SERVICE_ID",
  templateIdNotification: "YOUR_NOTIFICATION_TEMPLATE_ID", // Notification sent to you
  templateIdAutoresponder: "YOUR_AUTORESPONDER_TEMPLATE_ID", // Confirmation sent to client
  yourWhatsappNumber: "918870341570" // Your business WhatsApp number (with country code, no spaces/plus)
};

const isEmailjsConfigured = emailjsConfig.publicKey && emailjsConfig.publicKey !== "YOUR_EMAILJS_PUBLIC_KEY";

// Backward compatibility configuration wrapper for subpages
const firebaseConfig = {
  googleSheetUrl: "https://script.google.com/macros/s/AKfycbxKjMNtXAiBRuvexb0FZBLry4Bp8BBIQluqb0Nqva0GTr4VbHikkEgfxrsYghVMRFfD/exec"
};

// Google Sheets Web App URL (for index.html compatibility)
const googleSheetUrl = firebaseConfig.googleSheetUrl;

const isGoogleSheetConfigured = googleSheetUrl && googleSheetUrl !== "YOUR_GOOGLE_SCRIPT_URL";

/*
=============================================================================
GOOGLE SHEETS APPS SCRIPT SETUP INSTRUCTIONS:
1. Create a new Google Sheet.
2. In Google Sheets menu: Go to Extensions -> Apps Script.
3. Delete any code inside Code.gs and paste the following script:

function doPost(e) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var p = e.parameter;
  var method = p.contactMethod || "General";
  var sheetName = method === "WhatsApp" ? "WhatsApp Leads" : "Email Leads";
  var sheet = ss.getSheetByName(sheetName);
  
  if (!sheet) {
    sheet = ss.insertSheet(sheetName);
    sheet.appendRow(["Date", "Name", "Email", "WhatsApp", "Preference", "Message", "Source Page"]);
  }
  
  sheet.appendRow([
    new Date().toLocaleString(),
    p.name,
    p.email,
    p.whatsapp,
    method,
    p.question,
    p.sourcePage || "Unknown"
  ]);
  
  return ContentService.createTextOutput("SUCCESS");
}

4. Click "Deploy" button (top right) -> "New deployment".
5. Select Type: "Web app".
6. Description: "Boldlabs Leads Web App".
7. Execute as: "Me" (your email).
8. Who has access: "Anyone".
9. Click "Deploy". Authorize permissions if prompted.
10. Copy the "Web app URL" and paste it in the "googleSheetUrl" config variable above.
=============================================================================
*/
