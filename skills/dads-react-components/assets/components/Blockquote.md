# Blockquote

元のフォルダ: `src/components/Blockquote/`。`scripts/add_components.py` で個別のファイルに展開できる。

<!-- file: Blockquote.tsx -->
````tsx
import type { ComponentProps } from 'react';

type Props = ComponentProps<'blockquote'>;

export const Blockquote = (props: Props) => {
  const { children, className, ...rest } = props;
  return (
    <blockquote
      className={`border-l-8 border-solid-gray-536 py-2 pl-6 pr-4 mx-10 [&>*:first-child]:!mt-0 [&>*:last-child]:!mb-0 ${className ?? ''}`}
      {...rest}
    >
      {children}
    </blockquote>
  );
};
````

<!-- file: index.ts -->
````ts
export { Blockquote } from './Blockquote';
````
