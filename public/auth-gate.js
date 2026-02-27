/**
 * auth-gate.js — Centralised authentication gate
 *
 * Loaded as is:inline in <body> so it re-runs on every ViewTransition
 * navigation. Redirects unauthenticated users to /login on protected pages.
 * Client-side only — this is for tracking engagement, not protecting secrets.
 */
(function () {
  var root = document.documentElement;
  var path = window.location.pathname.replace(/\/$/, '') || '/';
  var publicPaths = ['/', '/login'];

  /* Public pages — show content immediately, no auth needed */
  if (publicPaths.indexOf(path) !== -1) {
    root.classList.add('authed');
    return;
  }

  /* Protected page — hide content until auth is confirmed.
     Remove authed class first (may linger from a previous public page). */
  root.classList.remove('authed');

  function checkAuth() {
    if (!window._bioAuth) {
      setTimeout(checkAuth, 100);
      return;
    }

    /* If user already resolved from a previous page, use cached value */
    if (window._bioCurrentUser) {
      root.classList.add('authed');
      return;
    }

    var unsubscribe = window._bioAuth.onAuthStateChanged(function (user) {
      unsubscribe();
      if (!user) {
        window.location.href = '/login?redirect=' +
          encodeURIComponent(window.location.pathname + window.location.search);
      } else {
        root.classList.add('authed');
      }
    });
  }

  checkAuth();
})();
