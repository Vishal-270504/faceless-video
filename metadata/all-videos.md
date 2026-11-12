# Metadata for all videos

Each entry: title, description, thumbnail prompt for ChatGPT (image generation, 1080x1920). ChatGPT sometimes misspells text in images. If it does, regenerate or fix the text in an image editor.

---

## 1. ux-5-states: The 5 UX states every app needs

**Title:** Your App Looks Broken Without These 5 States

**Description:**
Your app shows a blank screen, and users think it's broken, even when the code works. Every screen needs five states: loading, empty, error, offline and not found. Here's how to show each one in plain words.

#react #webdev #uxdesign #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "BLANK SCREEN = BUG?" with "BUG?" in yellow. Centre: a flat, minimal illustration of a phone showing an empty white screen with one small grey placeholder card. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 2. ux-details: 5 small UX details that make an app feel professional

**Title:** 5 Small UX Details That Make Your App Feel Professional

**Description:**
Two apps can do the same job, but one feels cheap and the other feels professional. The difference is small details: field-level errors, a delete confirmation, clear feedback, helper text and accessibility. Each one takes minutes to add.

#react #webdev #uxdesign #accessibility #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Top: small blue label "5 DETAILS" and five short segments in a row, the first two filled. Centre: a minimal dark UI card with a delete confirmation dialog, the "Cancel" button outlined in blue and a red "Delete" button. Large bold white text below: "SMALL DETAILS." and "BIG DIFFERENCE." Flat design, crisp edges, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 3. cors-failed-to-fetch: "Failed to fetch" in React? It's probably CORS

**Title:** "Failed to fetch" in React? It's Probably CORS

**Description:**
Your login fails with "Failed to fetch," but your code looks fine. The real reason is in the browser console: CORS. Your app and your API run on different addresses, and the API has to allow your app's address. Here's how to find it and fix it.

#react #cors #webdev #debugging #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "FAILED TO FETCH?" with "FETCH?" in red. Centre: a flat illustration of a browser window in the middle, a red blocked-arrow between two small boxes labelled "APP" and "API", and a dark console panel below with one red line of text. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 4. react-typing-lag: Why your React app gets slow when you type

**Title:** Why Your React App Gets Slow When You Type

**Description:**
Every keystroke re-renders the whole page, including every note card. With ten notes, each letter can cost about 200 milliseconds. Here's the fix: move the form's state into its own component, memoize the cards, and keep the handlers stable. And why memo doesn't fix everything.

#react #reactjs #webdev #performance #frontend #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "LAGGY TYPING?" with "LAGGY" in red. Centre: a flat illustration of a text input with a cursor, and below it a grid of ten small grey cards, with a red bar at the bottom reading "200 ms per letter". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 5. dark-mode-react: Dark mode in React in 5 minutes (done right)

**Title:** Dark Mode in React: Stop Hard-Coding Colors

**Description:**
Most broken dark modes only change the background, so the text becomes unreadable. The fix: every color comes from one place, as a CSS variable. Define the dark values once, add a toggle that remembers the choice, and use the system setting as the default.

#react #darkmode #css #webdev #frontend #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "DARK MODE BROKEN?" with "BROKEN?" in red. Centre: two flat mini app cards side by side, the left one black with almost invisible grey text, the right one dark with bright readable text, and a toggle switch below the right card in blue. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 6. idor-notes-app: Your API might leak other users' data (IDOR)

**Title:** Your API Might Leak Other Users' Data (IDOR)

**Description:**
Logging in proves who you are. The server still has to check that the item belongs to you. Without that check, anyone can change a number in the URL and read or delete someone else's note. This is called an IDOR. Here's how to stop it, and why the server should return 404, not 403.

#security #api #webdev #backend #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "ANYONE CAN READ IT" with "READ" in red. Centre: a flat browser address bar showing a URL ending in a highlighted number, with a small red lock icon and a flat note card beneath it marked "PRIVATE". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 7. cache-invalidation: Why your API returns old data

**Title:** Why Your API Returns Old Data (Cache Invalidation)

**Description:**
You create a note, but the list doesn't show it. The API is answering from a cache that's out of date. Here's how to spot it with the X-Cache header, and how a version number in the cache key fixes it for just one user.

#backend #caching #api #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "STILL MISSING?" with "MISSING?" in yellow. Centre: a flat list of three note rows with a fourth faint row marked with a dashed outline, beside a small badge reading "X-Cache: HIT" in red. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 8. clean-architecture-aspnet: Clean architecture in ASP.NET Core

**Title:** Clean Architecture in ASP.NET Core: One Rule, One Place

**Description:**
Your controller checks for 5 characters while your service checks for 3, and now the rule drifts apart. Here's a clean split: the controller handles HTTP, the service holds the rules, and the repository stores data. Every write goes through the service, and switching databases changes one line.

#aspnet #dotnet #csharp #architecture #webdev #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "ONE RULE. ONE PLACE." with "ONE PLACE." in blue. Centre: three flat stacked boxes labelled "CONTROLLER", "SERVICE" and "REPOSITORY", with arrows between them and a dashed red bypass arrow that is crossed out. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.
