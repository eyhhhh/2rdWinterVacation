import { useState } from "react";

function Accordion({title, content}){
  const [isOpend, setIsOpend] = useState(false);

  return(
    <div>
      <div style={{
        background: '#666',
        color: 'white',
        fontWeight: 'bold',
        padding: 10,
        display: 'flex',
        justfiyContent: 'space-between'
      }}
      onClick={()=>{
        setIsOpend(!isOpend);
      }}>
        <div>{title}</div>
        <div>{isOpend ? '-':'+'}</div>
      </div>

      {isOpend && (
        <div style={{
          border: '1px solid #999',
          padding: 20
        }}>{content}</div>
      )}
    </div>
  );
}

export default Accordion;