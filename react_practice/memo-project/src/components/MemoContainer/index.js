import './index.css';

function MemoContainer({ memo, setMemo }) {
  if (memo == undefined) {
    return (
      <div>
        <h1>메모가 없습니다.</h1>
        <h2>새로운 메모를 추가해주세요.</h2>
      </div>
    );
  }

  return (
    <div className="MemoContainer">
      <div>
        <input
          type="text"
          className="MemoContainer_title"
          value={memo.title}
          onChange={(e) => {
            setMemo({
              ...memo, // 다른 정보들은 유지
              title: e.target.value,
              updatedAt: new Date().getTime(),
            });
          }}
        />
      </div>
      <div>
        <textarea
          className="MemoContainer_content"
          value={memo.content}
          onChange={(e) => {
            setMemo({
              ...memo, // 다른 정보들은 유지
              content: e.target.value,
              updatedAt: new Date().getTime(),
            });
          }}
        />
      </div>
    </div>
  );
}

export default MemoContainer;
