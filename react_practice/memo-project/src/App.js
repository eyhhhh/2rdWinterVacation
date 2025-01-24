import { useState } from 'react';
import './App.css';
import MemoContainer from './components/MemoContainer';
import SideBar from './components/SideBar';

function App() {
  const [memos, setMemos] = useState([
    {
      title: 'Memo 1',
      content: 'This is memo 1',
      createdAt: 1737730385742,
      updatedAt: 1737730420708,
    },
    {
      title: 'Memo 2',
      content: 'This is memo 2',
      createdAt: 1737730487200,
      updatedAt: 1737730498197,
    },
  ]);

  const [selectedMemoIndex, setSelectedMemoIndex] = useState(0); // 초기값은 첫번째 메모 선택택

  const setMemo = (newMemo) => {
    const newMemos = [...memos];

    newMemos[selectedMemoIndex] = newMemo;
    setMemos(newMemos);
  };
  return (
    <div className="App">
      <SideBar
        memos={memos}
        selectedMemoIndex={selectedMemoIndex}
        setSelectedMemoIndex={setSelectedMemoIndex}
      />
      <MemoContainer memo={memos[selectedMemoIndex]} setMemo={setMemo} />
    </div>
  );
}

export default App;
