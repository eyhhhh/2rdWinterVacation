function SideBarFooter({ onClick }) {
  return (
    <div className="SideBarFooter">
      <button className="SideBarFooter_add-button" onClick={onClick}>
        +
      </button>
    </div>
  );
}

export default SideBarFooter;
