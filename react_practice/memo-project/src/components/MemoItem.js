function MemoItem({ children, onClickItem, onClickDelete, isSelcted }) {
  return (
    <div
      className={'MemoItem' + (isSelcted ? ' selected' : '')}
      onClick={onClickItem}
    >
      {children}
      <button className="MemoItem_delete-button" onClick={onClickDelete}>
        X
      </button>
    </div>
  );
}

export default MemoItem;
