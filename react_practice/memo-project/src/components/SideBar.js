import MemoList from './MemoList';
import SideBarFooter from './SideBarFooter';
import SideBarHeader from './SideBarHeader';

function SideBar({ memos, addMemo, selectedMemoIndex, setSelectedMemoIndex }) {
  return (
    <div className="SideBar">
      <SideBarHeader />
      <MemoList
        memos={memos}
        selectedMemoIndex={selectedMemoIndex}
        setSelectedMemoIndex={setSelectedMemoIndex}
      />
      <SideBarFooter onClick={addMemo} />
    </div>
  );
}

export default SideBar;
