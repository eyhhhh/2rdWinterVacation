export function setItem(key, value) {
  localStorage.setItem('memo', JSON.stringify(value));
}

export function getItem(key) {
  return JSON.parse(localStorage.getItem(key));
}
