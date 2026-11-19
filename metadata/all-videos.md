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

---

## 9. api-pagination: Pagination in a Notes API

**Title:** Pagination in APIs: Stop Sending Every Row

**Description:**
Your notes API sends every note in one response. It works with ten notes, then the app freezes at ten thousand. Pagination sends one page at a time, with a cap on the page size and a check on the numbers. Code: https://github.com/Vishal-270504/notes-app

#api #backend #typescript #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "TOO MUCH DATA?" with "DATA?" in yellow. Centre: a flat tall stack of thin grey rows that runs off the top of the frame, with a clean block of three rows highlighted in blue beneath it labelled "PAGE 1". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 10. api-validation: Validation in a Notes API

**Title:** API Validation: Stop Garbage at the Door

**Description:**
Someone sends a note with no title, and your API saves it anyway. Validation checks every request before it reaches the database, and rejects bad data with a clear 400 Bad Request. Code: https://github.com/Vishal-270504/notes-app

#api #backend #validation #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "GARBAGE IN?" with "IN?" in red. Centre: a flat door-shaped checkpoint in blue, with a red rejected box on one side and three clean green rows on the other, labelled "400". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 11. api-rate-limiting: Rate limiting in an API

**Title:** Rate Limiting: Stop One Client Taking Down Your API

**Description:**
One script can send a thousand requests a second, and your server slows down for everyone. Rate limiting gives each client a fixed number of requests per minute. Extra requests get a 429 Too Many Requests, so the rest of your users keep working. Code: https://github.com/Vishal-270504/notes-app

#api #backend #ratelimiting #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "429" in red with "TOO MANY" in white below it. Centre: a flat counter bar almost full in blue labelled "60 / minute", with a single red dot flying past it. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 12. api-error-handling: Error handling in an API

**Title:** API Error Handling: One Place, One Response

**Description:**
When something breaks, your API shouldn't show a wall of stack trace to the user. One central error handler turns every failure into one response shape: a clear status code and a short message. The full details stay in the server logs. Code: https://github.com/Vishal-270504/notes-app

#api #backend #errorhandling #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "SHOWING STACK TRACES?" with "STACK TRACES?" in red. Centre: a flat dark panel with three faint red error lines on the left, a single blue funnel in the middle, and one clean white card on the right labelled "404 Not found". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 13. auth-authentication: Authentication: How Your API Knows Who You Are

**Title:** Authentication: How Your API Knows Who You Are

**Description:**
Before your API does anything, it has to know who is calling. Passwords are stored as hashes, a correct login returns a signed token, and a missing or invalid token gets a 401. Here's the flow in plain words.

#api #backend #authentication #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "WHO ARE YOU?" with "YOU?" in yellow. Centre: a flat closed padlock above a small signed ticket card with a blue edge. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 14. auth-authorization: Authentication vs Authorization: Who Can Touch It?

**Title:** Logged In Isn't Enough: Check the Owner

**Description:**
Logging in proves who you are. It doesn't prove you may open someone else's note. Every action on user data needs an ownership check, and a request for someone else's data gets a 403.

#api #backend #authorization #security #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "CAN YOU TOUCH IT?" with "TOUCH" in yellow. Centre: a flat door with a padlock on it and a small red tag beside it labelled "403". Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 15. db-indexes: Why Your Query Is Slow (and How an Index Fixes It)

**Title:** Why Your Query Is Slow (Add an Index)

**Description:**
Your API can feel fast with ten rows and crawl with a hundred thousand. The database checks every row unless you tell it otherwise. You'll see how to measure a slow query, add an index, and what that index costs on writes.

#api #database #sql #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "SLOW QUERY?" with "SLOW" in yellow. Centre: a flat open book with small index tabs along its edge, one tab highlighted blue. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 16. aspnet-controller-service-repo: Controller, Service, Repository in ASP.NET Core

**Title:** Controller, Service, Repository in ASP.NET Core

**Description:**
A controller that handles routing, rules and database calls is hard to change. Split it into a controller, a service and a repository, and the API behaves exactly the same from the outside. Only the structure changes.

#aspnet #dotnet #csharp #cleancode #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "ONE CLASS DOES ALL?" with "ALL?" in yellow. Centre: three flat stacked boxes in blue, white and grey, joined by thin arrows, with the bottom box marked by a small cylinder icon. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 17. api-never-trust-client: Never Trust the Client: Stop Users Changing Your Data

**Title:** Never Trust the Client: Decide on the Server

**Description:**
Anyone can send any request to your API, even with your app's own tools. The server should choose the owner and the IDs, ignore what the client claims, and check ownership on every read, update and delete.

#api #backend #security #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "NEVER TRUST" with "TRUST" in yellow. Centre: a flat bank vault door in grey with a blue keyhole, and a small red "X" card floating beside it. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 18. api-cache-per-user: Cache a Notes List for 60 Seconds (MISS vs HIT)

**Title:** Cache a Notes List: MISS vs HIT Explained

**Description:**
Your API answers the same question over and over. A per-user cache saves the list for 60 seconds, shows a MISS and then a HIT, and a version number clears it after every change. You trade a little freshness for speed.

#api #backend #caching #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "MISS → HIT" with "HIT" in yellow. Centre: a flat white coffee cup on top of a stack of three blue cards, with a small clock icon beside it. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 19. ux-tap-targets: Your Buttons Are Too Small to Tap

**Title:** Your Buttons Are Too Small to Tap

**Description:**
You tap the tiny X and hit the wrong thing. The icon can look small, but the area that reacts to a finger has to be big. Here is the minimum size Apple and Google suggest, and how to add it without changing the look.

#uxdesign #mobile #accessibility #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "TOO SMALL?" with "SMALL?" in yellow. Centre: a flat phone outline with one small X icon and a dashed blue square of 44 points around it. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 20. ux-hover-only-actions: Hover-Only Buttons Vanish on Phones

**Title:** Hover-Only Buttons Vanish on Phones

**Description:**
Edit and delete icons that appear only on hover look great on a laptop. On a phone there is no hover, so users cannot find those actions at all. Here is how to show them, and how to use hover as a bonus.

#uxdesign #mobile #webdev #frontend #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "NO HOVER?" with "HOVER?" in yellow. Centre: a flat phone outline showing one list row with a faint, dashed trash icon that is barely visible. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 21. ux-thumb-zone: Put Your Main Button Where the Thumb Rests

**Title:** Put Your Main Button Where the Thumb Rests

**Description:**
Most people hold their phone in one hand, and the top corners are a stretch. Your most-used button should sit at the bottom, where the thumb already rests. Here is how to move it and what to keep up top.

#uxdesign #mobile #ios #android #webdev #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "THUMB REACH" with "REACH" in yellow. Centre: a flat phone outline, the bottom half shaded green and the top right corner shaded red, with one white thumb circle at the bottom. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 22. ux-button-labels: Stop Using OK and Cancel: Name the Action

**Title:** Stop Using OK and Cancel: Name the Action

**Description:**
A dialog that says OK and Cancel makes users guess what happens next. A button label should say the action itself, in a verb. Here are the words to swap out, and the ones to avoid.

#uxdesign #uxwriting #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "OK? CANCEL?" with "OK?" in yellow. Centre: a flat dialog box with a question line and two buttons, one reading "Publish note" in blue and one reading "Keep private" in outline. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 23. ux-one-primary-button: One Loud Button Per Screen

**Title:** One Loud Button Per Screen

**Description:**
When every button on a screen looks the same, users do not know what to do first. Give each screen one primary action, make the rest quieter, and never style a delete like the main button.

#uxdesign #webdesign #ui #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "ONE LOUD BUTTON" with "LOUD" in yellow. Centre: a flat screen outline with one large solid blue button at the bottom and two thin outlined buttons above it. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 24. ux-contrast: Light Grey Text Is Invisible in Sunlight

**Title:** Light Grey Text Is Invisible in Sunlight

**Description:**
Text that looks fine on a big monitor can disappear on a bright phone screen. The cause is low contrast between text and background. Here is how to measure it, what ratio to aim for, and the quick fix.

#uxdesign #accessibility #webdev #css #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "CAN YOU READ IT?" with "READ" in yellow. Centre: a flat white card with a faint grey date line, and a small red label beside it reading "2.8 : 1". Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 25. ux-autosave-notes: Never Make Users Save Their Notes by Hand

**Title:** Never Make Users Save Their Notes by Hand

**Description:**
A note app with only a Save button loses words when the user forgets to tap it or the phone dies. Autosave the draft after a short pause, and show a status line so users know their words are safe.

#uxdesign #notesapp #webdev #javascript #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "LOST YOUR NOTE?" with "NOTE?" in yellow. Centre: a flat editor card with three short text lines and a green dot followed by a line reading "Saved". Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 26. ux-optimistic-update: Like Feels Slow? Update Before the Server

**Title:** Like Feels Slow? Update Before the Server

**Description:**
A button that waits for the server feels broken, and users tap it twice. Optimistic UI updates the screen at once and sends the request in the background. If the server says no, roll back and say why.

#uxdesign #webdev #react #javascript #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "TAP. WAIT. TAP." with "WAIT." in yellow. Centre: a flat note card with one green button labelled "Liked" and a small grey pill labelled "Syncing". Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 27. ux-search-as-you-type: Why Your Search Sends 10 Requests

**Title:** Why Your Search Sends 10 Requests

**Description:**
Live search that calls the server on every keystroke wastes work and slows the screen. Debounce it: wait for a short pause, then search once. The box keeps focus, and the results update as the user types.

#uxdesign #webdev #javascript #search #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "10 REQUESTS?" with "10" in yellow. Centre: a flat search bar with a row of ten small red squares below it, and a single blue bar labelled as a pause on the right. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 28. ux-focus-after-dialog: Close a Dialog Without Losing Your Place

**Title:** Close a Dialog Without Losing Your Place

**Description:**
After a dialog closes, the cursor jumps to the top of the page and keyboard users are lost. Move focus into the dialog when it opens, keep Tab inside it, and send focus back to the button that opened it when it closes.

#accessibility #uxdesign #webdev #frontend #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "LOST FOCUS?" with "FOCUS?" in yellow. Centre: a flat page with three buttons, one outlined in a thick blue focus ring, and a small dialog box above them. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 29. fe-what-is-dom: What Is the DOM? The Page Behind Your Screen

**Level:** Beginner

**Title:** What Is the DOM? The Page Behind Your Screen

**Description:**
Your browser turns HTML into a live tree called the DOM, and JavaScript changes that tree to update the screen. This short shows what a node is, why changing the HTML file does not change the open page, and how to explore the DOM with your browser's inspect tool.

Background video: Coverr-Free-Footage on Pixabay (https://pixabay.com/videos/id-4733/), Pixabay Content License.

#frontend #webdev #javascript #beginner #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background with a teal (#2ec4b6) accent. Large bold white text across the top: "WHAT IS THE DOM?" with "DOM?" in teal. Centre: a flat tree diagram of three small rounded boxes (html, body, button) linked by thin teal lines. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 30. fe-css-box-model: Why Your Box Is Bigger Than You Set (Box Model)

**Level:** Beginner

**Title:** Why Your Box Is Bigger Than You Set

**Description:**
You set a box to 300 pixels and it measures 342 on screen. The CSS box model adds padding and border to the width, and border-box fixes it with one rule. This video walks through the four layers and the math.

Background video: QuinceCreative on Pixabay (https://pixabay.com/videos/id-12919/), Pixabay Content License.

#css #frontend #webdev #beginner #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background with an orange (#ff9f1c) accent. Large bold white text across the top: "BIGGER THAN 300?" with "300?" in orange. Centre: a flat dashed rectangle labelled "300" with a solid orange rectangle slightly larger around it, showing the extra space. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 31. fe-flexbox-center: Center Anything in CSS with Flexbox

**Level:** Beginner

**Title:** Center Anything in CSS with Flexbox

**Description:**
Centering a box both ways used to take hours of guessing. Flexbox does it with three properties: display flex on the parent, justify-content, and align-items. This video shows the broken margin version first, then the fix.

Background video: ArtSqb on Pixabay (https://pixabay.com/videos/id-9809/), Pixabay Content License.

#css #flexbox #frontend #webdev #beginner #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background with a green (#7bd389) accent. Large bold white text across the top: "CENTER IT" with "CENTER" in green. Centre: a flat dashed rectangle with one small green square exactly in its middle, with thin crosshair lines through it. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 32. fe-async-await: Why Your Data Says undefined (async and await)

**Level:** Intermediate

**Title:** Why Your Data Says undefined: async/await

**Description:**
You fetch data, log it, and it says undefined because your code ran before the response arrived. The fix is await, plus a check on response.ok, since a 404 still resolves. This video shows the timeline behind the bug.

Background video: cipnt on Pixabay (https://pixabay.com/videos/id-14900/), Pixabay Content License.

#javascript #async #webdev #frontend #intermediate #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black navy background with a sky-blue (#4cc9f0) accent. Large bold white text across the top: "UNDEFINED?" with "UNDEFINED?" in sky blue. Centre: two flat horizontal timeline bars, one short (JavaScript) and one long (network), with a small sky-blue dot at the start of the short bar. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 33. fe-closures: JavaScript Closures in 60 Seconds

**Level:** Intermediate

**Title:** JavaScript Closures in 60 Seconds

**Description:**
A closure is a function that remembers the variables around it, even after the outer function has finished. This short builds a counter step by step, shows why the count is not reset, and shows the loop-of-buttons case that trips up beginners.

Background video: MotionVision on Pixabay (https://pixabay.com/videos/id-47712/), Pixabay Content License.

#javascript #closures #webdev #frontend #intermediate #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black indigo background with a violet (#b388ff) accent. Large bold white text across the top: "IT REMEMBERS" with "REMEMBERS" in violet. Centre: a flat rounded box containing a small violet square labelled "count", with a dashed inner box beside it. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 34. fe-css-grid: Build a Page Layout with CSS Grid

**Level:** Intermediate

**Title:** Build a Page Layout with CSS Grid

**Description:**
A header, a sidebar and a main area sound simple, but fixed widths break on a phone. CSS Grid defines the whole page as rows and columns, with named areas, and stacks on mobile with one line of CSS. This short shows the overflow bug, the fix, and when to use Flexbox instead.

Background video: doktorkleinmusic on Pixabay (https://pixabay.com/videos/id-326417/), Pixabay Content License.

#css #grid #frontend #webdev #intermediate #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background with an amber (#ffd166) accent. Large bold white text across the top: "PAGE LAYOUT" with "LAYOUT" in amber. Centre: a flat wireframe of a web page with a wide header box on top, a narrow box on the left and a wide box on the right. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 35. fe-react-keys: The React Key Bug That Shows the Wrong Row

**Level:** Intermediate

**Title:** The React Key Bug That Shows the Wrong Row

**Description:**
You delete an item and the wrong row changes, or typed text jumps to another item. Using the array index as a key is the usual cause. This short shows why React matches rows by position and how a stable ID fixes it.

Background video: Coverr-Free-Footage on Pixabay (https://pixabay.com/videos/id-3180/), Pixabay Content License.

#react #javascript #webdev #frontend #intermediate #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background with a pink (#ff5d8f) accent. Large bold white text across the top: "WRONG ROW?" with "WRONG" in pink. Centre: a flat list of three rows, with small pink key tags on the right of each row, and the top row marked with a flat red X. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 36. fe-useeffect-cleanup: Stop the Leak: useEffect Cleanup Explained

**Level:** Advanced

**Title:** Stop the Leak: useEffect Cleanup Explained

**Description:**
A timer started in useEffect keeps running after the page is gone, and that is a memory leak. Return a cleanup function from the effect to clear the interval or remove the listener. This short shows the leak, the cleanup, and why React runs effects twice in development.

Background video: MattHrusc on Pixabay (https://pixabay.com/videos/id-26452/), Pixabay Content License.

#react #hooks #javascript #webdev #advanced #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black olive background with a lime (#c6f432) accent. Large bold white text across the top: "STILL RUNNING?" with "RUNNING?" in lime. Centre: a flat rounded box showing a large lime number, with a flat line of arrows running out of it toward a small X. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 37. fe-web-workers: Stop Your Page Freezing with Web Workers

**Level:** Advanced

**Title:** Stop Your Page Freezing with Web Workers

**Description:**
Heavy JavaScript on the main thread freezes the page and every click waits in line. A Web Worker runs the work in a background thread and sends the result back with postMessage. This short shows the blocked thread, the worker lane, and the one thing workers cannot do: touch the DOM.

Background video: onijake on Pixabay (https://pixabay.com/videos/id-13461/), Pixabay Content License.

#javascript #webworkers #performance #webdev #advanced #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background with an ember (#ff7a45) accent. Large bold white text across the top: "PAGE FROZEN?" with "FROZEN?" in ember. Centre: two flat horizontal lanes, the top one fully orange and blocked, and the bottom lane split, with a clear green free area on the top. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 38. fe-lazy-images: Why Your Page Loads 40 Images Before Scroll

**Level:** Advanced

**Title:** Why Your Page Loads 40 Images Before Scroll

**Description:**
A page that downloads every image on open is slow on a phone, and most of those images are off screen. Add loading="lazy" to images below the fold, keep the hero eager, and set width and height so the layout does not jump. This short shows each step.

Background video: AttilaPergel on Pixabay (https://pixabay.com/videos/id-111280/), Pixabay Content License.

#webperformance #frontend #html #webdev #advanced #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black indigo background with an indigo (#a5b4fc) accent. Large bold white text across the top: "40 IMAGES?" with "40" in indigo. Centre: a flat grid of small square tiles, the top rows solid indigo and the lower rows dashed outlines, with a dashed horizontal line marking the screen edge. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.
