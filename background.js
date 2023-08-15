// background.js

let color = '#3a3ca7';

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ color });
  console.log('Default background color set to %cblue', `color: ${color}`);
});