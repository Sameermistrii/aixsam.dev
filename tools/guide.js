// Copy buttons on every command block in the setup guides.
document.querySelectorAll('pre').forEach(pre => {
  const b = Object.assign(document.createElement('button'), {type: 'button', className: 'copy', textContent: 'Copy'});
  b.setAttribute('aria-label', 'Copy command');
  b.onclick = () => navigator.clipboard.writeText(pre.querySelector('code').innerText.trim())
    .then(() => { b.textContent = 'Copied ✓'; setTimeout(() => (b.textContent = 'Copy'), 1500); })
    .catch(() => { b.textContent = 'Select & copy'; });
  pre.append(b);
});
