function MemoItem({ children, onClick, isSelcted }) {
  return (
    <div
      className={'MemoItem' + (isSelcted ? ' selected' : '')}
      onClick={onClick}
    >
      {children}
    </div>
  );
}

export default MemoItem;
