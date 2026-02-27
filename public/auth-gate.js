/**
 * auth-gate.js — Centralised authentication gate
 *
 * Included in BaseLayout after Firebase init. Automatically redirects
 * unauthenticated users to /login on all pages except public ones.
 * Client-side only — this is for tracking engagement, not protecting secrets.
 */
(function () {
  var path = window.location.pathname.replace(/\/$/, '') || '/';
  var publicPaths = ['/', '/login'];

  if (publicPaths.indexOf(path) !== -1) {
    document.body.classList.add('authed');
    return;
  }

  function checkAuth() {
    if (!window._bioAuth) {
      setTimeout(checkAuth, 100);
      return;
    }

    /* If user already resolved, use cached value */
    if (window._bioCurrentUser) {
      document.body.classList.add('authed');
      return;
    }

    var unsubscribe = window._bioAuth.onAuthStateChanged(function (user) {
      unsubscribe();
      if (!user) {
        window.location.href = '/login?redirect=' +
          encodeURIComponent(window.location.pathname + window.location.search);
      } else {
        document.body.classList.add('authed');
      }
    });
  }

  checkAuth();
})();
