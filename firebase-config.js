// Firebase configuration keys (Replace with your actual Firebase Project config)
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Check if configuration has been updated from placeholders
const isFirebaseConfigured = firebaseConfig.apiKey && firebaseConfig.apiKey !== "YOUR_API_KEY";

let db = null;
let auth = null;

if (isFirebaseConfigured) {
  try {
    firebase.initializeApp(firebaseConfig);
    db = firebase.firestore();
    auth = firebase.auth();
    console.log("Firebase initialized successfully.");
  } catch (error) {
    console.error("Firebase initialization failed:", error);
  }
} else {
  console.warn("Firebase credentials are not set. Running in Local Mock Storage mode.");
}

// EmailJS configuration keys (Replace with your actual EmailJS credentials)
const emailjsConfig = {
  publicKey: "YOUR_EMAILJS_PUBLIC_KEY",
  serviceId: "YOUR_EMAILJS_SERVICE_ID",
  templateIdNotification: "YOUR_NOTIFICATION_TEMPLATE_ID", // Notification sent to you
  templateIdAutoresponder: "YOUR_AUTORESPONDER_TEMPLATE_ID", // Confirmation sent to client
  yourWhatsappNumber: "918870341570" // Your business WhatsApp number (with country code, no spaces/plus)
};

const isEmailjsConfigured = emailjsConfig.publicKey && emailjsConfig.publicKey !== "YOUR_EMAILJS_PUBLIC_KEY";

// Google Sheets Web App URL (Replace with your actual Google Apps Script URL)
const googleSheetUrl = "https://script.google.com/macros/s/AKfycbxKjMNtXAiBRuvexb0FZBLry4Bp8BBIQluqb0Nqva0GTr4VbHikkEgfxrsYghVMRFfD/exec";

const isGoogleSheetConfigured = googleSheetUrl && googleSheetUrl !== "YOUR_GOOGLE_SCRIPT_URL";

/*
=============================================================================
GOOGLE SHEETS APPS SCRIPT SETUP INSTRUCTIONS:
1. Create a new Google Sheet.
2. Add these headers in row 1: Date | Name | Email | WhatsApp | Preference | Message
3. In Google Sheets menu: Go to Extensions -> Apps Script.
4. Delete any code inside Code.gs and paste the following script:

function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var p = e.parameter;
  sheet.appendRow([
    new Date().toLocaleString(),
    p.name,
    p.email,
    p.whatsapp,
    p.contactMethod,
    p.question
  ]);
  return ContentService.createTextOutput("SUCCESS");
}

5. Click "Deploy" button (top right) -> "New deployment".
6. Select Type: "Web app".
7. Description: "Boldlabs Leads Web App".
8. Execute as: "Me" (your email).
9. Who has access: "Anyone".
10. Click "Deploy". Authorize permissions if prompted.
11. Copy the "Web app URL" and paste it in the "googleSheetUrl" config variable above.
=============================================================================
*/
