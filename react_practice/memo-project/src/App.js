import { useCallback, useState } from 'react';
import './App.css';
import MemoContainer from './components/MemoContainer'; // 알아서 index.js을 불러옴
import SideBar from './components/SideBar';
import { setItem, getItem } from './lib/storage';
import debounce from 'lodash.debounce';

const debouncedSetItem = debounce(setItem, 5000); // 호출 5초 뒤에 실행

function App() {
  const [memos, setMemos] = useState(getItem('memo') || []); // localstorage가 null인 경우 아무것도 안뜨는 걸 방지.

  const [selectedMemoIndex, setSelectedMemoIndex] = useState(0); // 초기값은 첫번째 메모 선택택

  const setMemo = useCallback(
    (newMemo) => {
      setMemos((memos) => {
        const newMemos = [...memos];

        newMemos[selectedMemoIndex] = newMemo;
        debouncedSetItem('memo', newMemos);
        //localStorage.setItem('memo', JSON.stringify(newMemos));

        return newMemos;
      });
    },
    [selectedMemoIndex], // dependencies
  );

  const addMemo = useCallback(() => {
    setMemos((memos) => {
      const now = new Date().getTime();

      const newMemos = [
        ...memos,
        {
          title: 'Untitled',
          content: '',
          createdAt: now,
          updatedAt: now,
        },
      ];

      debouncedSetItem('memo', newMemos);

      return newMemos;
    });
    setSelectedMemoIndex(memos.length);
  }, [memos]);

  const deleteMemo = useCallback(
    (index) => {
      setMemos((memos) => {
        const newMemos = [...memos]; // 불변성때문에 따로 생성성

        newMemos.splice(index, 1); // index요소를 1개 삭제

        debouncedSetItem('memo', newMemos);

        return newMemos;
      });
      if (index == selectedMemoIndex) {
        setSelectedMemoIndex(0);
      }
    },
    [selectedMemoIndex],
  );

  return (
    <div className="App">
      <SideBar
        memos={memos}
        addMemo={addMemo}
        selectedMemoIndex={selectedMemoIndex}
        setSelectedMemoIndex={setSelectedMemoIndex}
        deleteMemo={deleteMemo}
      />
      <MemoContainer memo={memos[selectedMemoIndex]} setMemo={setMemo} />
    </div>
  );
}

export default App;
